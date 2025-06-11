# Create your views here.
# myapp/views.py
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
# from .models import Case, Order, OrderItem
from .serializers import MTBBikeSerializer, RoadBikeSerializer, \
    FrameSerializer, ForkSerializer, WheelSetSerializer, CranksetSerializer, \
    BottomBracketSerializer, DerailleurSerializer, ShifterSerializer, \
    CassetteSerializer, ChainSerializer, TyreSerializer, HandlebarSerializer, \
    StemSerializer, BrakeSerializer, BrakeRotorSerializer  # , OrderSerializer, OrderItemSerializer
from .models import MTBBike, RoadBike, Frame, Fork, WheelSet, Crankset, BottomBracket, Derailleur, Shifter, Cassette, \
    Chain, Tyre, HandlebarFlat, Stem, Handlebar, Brakes, BrakeRotor
from django.db.models import F, ExpressionWrapper, FloatField
from django.db.models.functions import Abs
from rest_framework import mixins, viewsets


class MTBBikeViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = MTBBike.objects.all()
    serializer_class = MTBBikeSerializer

    @swagger_auto_schema(operation_summary="List All MTB Bikes")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Retrieve a Single MTB Bike")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    # @swagger_auto_schema(operation_summary="Create a New MTB Bike")
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)


#
#     @swagger_auto_schema(operation_summary="Retrieve Case Details by ID")
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#
#     @swagger_auto_schema(operation_summary="Update Case Details by ID")
#     def update(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     @swagger_auto_schema(operation_summary="Delete a Case by ID")
#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

class RoadBikeViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = RoadBike.objects.all()
    serializer_class = RoadBikeSerializer

    @swagger_auto_schema(operation_summary="List All Road Bikes")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Retrieve a Single Road Bike")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    # @swagger_auto_schema(operation_summary="Create a New Road Bike")
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)


class FrameRecommendationAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="GET рекомендовані рами на основі зросту та висоти ноги",
        manual_parameters=[
            openapi.Parameter('discipline', openapi.IN_QUERY, description="ID дисципліни", type=openapi.TYPE_INTEGER,
                              required=True),
            openapi.Parameter('height', openapi.IN_QUERY, description="Зріст користувача (в см)",
                              type=openapi.TYPE_NUMBER, required=True),
            openapi.Parameter('inseam', openapi.IN_QUERY, description="Висота ноги (в см)", type=openapi.TYPE_NUMBER,
                              required=True),
        ]
    )
    def get(self, request):
        try:
            discipline_id = request.GET.get('discipline')
            height = request.GET.get('height')
            inseam = request.GET.get('inseam')

            if not (discipline_id and height and inseam):
                return Response({"error": "Всі параметри (discipline, height, inseam) є обов’язковими."},
                                status=status.HTTP_400_BAD_REQUEST)

            discipline_id = int(discipline_id)
            height = float(height)
            inseam = float(inseam)

            target_seatpost = inseam * 0.65

            frames = Frame.objects.filter(
                application_id=discipline_id,
                min_rider_height__lte=height,
                max_rider_height__gte=height
            ).annotate(
                seatpost_diff=Abs(F('seatpost') - target_seatpost)
            ).order_by('seatpost_diff')

            serializer = FrameSerializer(frames, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ValueError:
            return Response({"error": "Некоректні числові значення параметрів."},
                            status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": f"Внутрішня помилка сервера: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ForkRecommendationAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="GET рекомендовані вилки на основі обраної рами (допуск ходу ±10 мм)",
        manual_parameters=[
            openapi.Parameter('frame_id', openapi.IN_QUERY, description="ID рами", type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self, request):
        try:
            frame_id = request.GET.get('frame_id')
            if not frame_id:
                return Response({"error": "Missing frame_id parameter."}, status=status.HTTP_400_BAD_REQUEST)

            frame = get_object_or_404(Frame, pk=frame_id)

            forks = Fork.objects.filter(
                wheel_size=frame.wheel_size,
                steerer_type=frame.steerer_type
                # axle_type=frame.axle_type,
                # brake_mount=frame.brake_mount
            )

            # Допуск ±10мм
            if frame.fork_travel:
                forks = forks.filter(
                    travel__gte=frame.fork_travel - 10,
                    travel__lte=frame.fork_travel + 10
                )

            serializer = ForkSerializer(forks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CranksetRecommendationAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Отримати сумісні шатунні системи за ID рами",
        manual_parameters=[
            openapi.Parameter('frame_id', openapi.IN_QUERY, description="ID вибраної рами", type=openapi.TYPE_INTEGER),
            # openapi.Parameter('gearing', openapi.IN_QUERY, description="Кількість передач (наприклад, 12 для 1x12)",
            #                   type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self, request):
        try:
            frame_id = request.GET.get('frame_id')
            # gearing = request.GET.get('gearing')

            if not frame_id:  # or not gearing:
                return Response({"error": "Потрібні параметри 'frame_id'"},  # та 'gearing'.
                                status=status.HTTP_400_BAD_REQUEST)

            frame = Frame.objects.filter(id=frame_id).first()
            if not frame or not frame.chainline:
                return Response({"error": "Раму не знайдено або вона не має відповідний chainline."},
                                status=status.HTTP_404_NOT_FOUND)

            chainline = float(frame.chainline)
            # gearing = int(gearing)

            cranksets = Crankset.objects.filter(
                # gearing=gearing,
                chainline__gte=chainline - 1,
                chainline__lte=chainline + 1
            )

            serializer = CranksetSerializer(cranksets, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ValueError:
            return Response({"error": "Неправильні типи параметрів."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BottomBracketRecommendationAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Підбір каретки за рамою та шатуном",
        manual_parameters=[
            openapi.Parameter('frame_id', openapi.IN_QUERY, description="ID рами", type=openapi.TYPE_INTEGER),
            openapi.Parameter('crankset_id', openapi.IN_QUERY, description="ID шатунів", type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self, request):
        try:
            frame_id = request.GET.get("frame_id")
            crankset_id = request.GET.get("crankset_id")

            if not frame_id or not crankset_id:
                return Response({"error": "Missing frame_id or crankset_id"}, status=status.HTTP_400_BAD_REQUEST)

            frame = Frame.objects.get(id=frame_id)
            crankset = Crankset.objects.get(id=crankset_id)

            # Підбір за типом, діаметром осі та шириною оболонки (допуск ±1 мм)
            brackets = BottomBracket.objects.filter(
                type=frame.bb_standard.bb_name,
                axle_diameter=crankset.axle_diameter,
                shell_width__gte=frame.bb_standard.shell_width - 1,
                shell_width__lte=frame.bb_standard.shell_width + 1
            )

            serializer = BottomBracketSerializer(brackets, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Frame.DoesNotExist:
            return Response({"error": "Frame not found"}, status=status.HTTP_404_NOT_FOUND)
        except Crankset.DoesNotExist:
            return Response({"error": "Crankset not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DerailleurRecommendationAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Отримати сумісні задні перемикачі за ID шатунів",
        manual_parameters=[
            openapi.Parameter(
                'crankset_id',
                openapi.IN_QUERY,
                description="ID обраних шатунів",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ]
    )
    def get(self, request):
        try:
            crankset_id = request.GET.get("crankset_id")
            if not crankset_id:
                return Response({"error": "Параметр 'crankset_id' обов’язковий."}, status=status.HTTP_400_BAD_REQUEST)

            # Спроба отримати шатуни
            crankset = Crankset.objects.get(pk=crankset_id)
            gearing = crankset.gearing

            # Підбір перемикачів за кількістю передач
            derailleur_qs = Derailleur.objects.filter(gearing=gearing)
            serializer = DerailleurSerializer(derailleur_qs, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Crankset.DoesNotExist:
            return Response({"error": "Шатуни з таким ID не знайдено."}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"error": "Неправильний формат 'crankset_id'."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ShifterByDerailleurAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Підібрати шифтери за вибраним перемикачем",
        manual_parameters=[
            openapi.Parameter('derailleur_id', openapi.IN_QUERY, description="ID вибраного перемикача",
                              type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self, request):
        derailleur_id = request.GET.get("derailleur_id")

        if not derailleur_id:
            return Response({"error": "Потрібно вказати derailleur_id"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            derailleur = Derailleur.objects.get(id=derailleur_id)
        except Derailleur.DoesNotExist:
            return Response({"error": "Перемикач не знайдено"}, status=status.HTTP_404_NOT_FOUND)

        # Підбір шифтерів за кількістю передач
        shifters = Shifter.objects.filter(gearing=derailleur.gearing)

        serializer = ShifterSerializer(shifters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CassetteByDerailleurShifterAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Підібрати касети за перемикачем та манеткою",
        manual_parameters=[
            openapi.Parameter('derailleur_id', openapi.IN_QUERY, description="ID перемикача",
                              type=openapi.TYPE_INTEGER),
            openapi.Parameter('shifter_id', openapi.IN_QUERY, description="ID манетки", type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self, request):
        derailleur_id = request.GET.get("derailleur_id")
        shifter_id = request.GET.get("shifter_id")

        if not derailleur_id or not shifter_id:
            return Response({"error": "Необхідно передати derailleur_id і shifter_id"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            derailleur = Derailleur.objects.get(id=derailleur_id)
            shifter = Shifter.objects.get(id=shifter_id)
        except Derailleur.DoesNotExist:
            return Response({"error": "Перемикач не знайдено"}, status=status.HTTP_404_NOT_FOUND)
        except Shifter.DoesNotExist:
            return Response({"error": "Манетка не знайдена"}, status=status.HTTP_404_NOT_FOUND)

        # Підбір касет
        if derailleur.gearing != shifter.gearing:
            return Response({"error": "Gearing перемикача і манетки не співпадає"}, status=status.HTTP_400_BAD_REQUEST)

        cassettes = Cassette.objects.filter(
            gearing=derailleur.gearing,
            smallest_gear__gte=derailleur.smallest_gear,
            biggest_gear__lte=derailleur.biggest_gear,
        )

        serializer = CassetteSerializer(cassettes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChainByComponentsAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Підібрати ланцюги за касетою, перемикачем, шатунами та швидкістю",
        manual_parameters=[
            openapi.Parameter('cassette_id', openapi.IN_QUERY, description="ID касети", type=openapi.TYPE_INTEGER,
                              required=True),
            openapi.Parameter('derailleur_id', openapi.IN_QUERY, description="ID перемикача", type=openapi.TYPE_INTEGER,
                              required=True),
            openapi.Parameter('shifter_id', openapi.IN_QUERY, description="ID манетки", type=openapi.TYPE_INTEGER,
                              required=True),
            openapi.Parameter('crankset_id', openapi.IN_QUERY, description="ID шатунів", type=openapi.TYPE_INTEGER,
                              required=True),
        ]
    )
    def get(self, request):
        cassette_id = request.GET.get("cassette_id")
        derailleur_id = request.GET.get("derailleur_id")
        shifter_id = request.GET.get("shifter_id")
        crankset_id = request.GET.get("crankset_id")

        if not all([cassette_id, derailleur_id, shifter_id, crankset_id]):
            return Response({"error": "Необхідно передати cassette_id, derailleur_id, shifter_id і crankset_id"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            cassette = Cassette.objects.get(id=cassette_id)
            derailleur = Derailleur.objects.get(id=derailleur_id)
            shifter = Shifter.objects.get(id=shifter_id)
            crankset = Crankset.objects.get(id=crankset_id)
        except Cassette.DoesNotExist:
            return Response({"error": "Касета не знайдена"}, status=status.HTTP_404_NOT_FOUND)
        except Derailleur.DoesNotExist:
            return Response({"error": "Перемикач не знайдено"}, status=status.HTTP_404_NOT_FOUND)
        except Shifter.DoesNotExist:
            return Response({"error": "Манетка не знайдена"}, status=status.HTTP_404_NOT_FOUND)
        except Crankset.DoesNotExist:
            return Response({"error": "Шатуни не знайдені"}, status=status.HTTP_404_NOT_FOUND)

        # Перевірка сумісності gearing
        if not (cassette.gearing == derailleur.gearing == shifter.gearing == crankset.gearing):
            return Response({"error": "Gearing касети, перемикача, манетки і шатунів не співпадає"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Підбір ланцюгів за gearing (кількістю передач)
        chains = Chain.objects.filter(gearing=cassette.gearing)

        # За бажанням можна додати ще логіку фільтрації за типом замка, напрямком тощо

        serializer = ChainSerializer(chains, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WheelSetRecommendationAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Підібрати сумісний WheelSet за рамою, вилкою та касетою",
        manual_parameters=[
            openapi.Parameter('frame_id', openapi.IN_QUERY, description="ID рами", type=openapi.TYPE_INTEGER),
            openapi.Parameter('fork_id', openapi.IN_QUERY, description="ID вилки", type=openapi.TYPE_INTEGER),
            openapi.Parameter('cassette_id', openapi.IN_QUERY, description="ID касети", type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self, request):
        frame_id = request.GET.get('frame_id')
        fork_id = request.GET.get('fork_id')
        cassette_id = request.GET.get('cassette_id')

        if not frame_id or not fork_id or not cassette_id:
            return Response({"error": "Потрібно передати frame_id, fork_id та cassette_id"}, status=400)

        try:
            frame = Frame.objects.get(id=frame_id)
            fork = Fork.objects.get(id=fork_id)
            cassette = Cassette.objects.get(id=cassette_id)

            queryset = WheelSet.objects.filter(
                wheel_size=frame.wheel_size,
                front_wheel__front_hub__axle_type=fork.axle_type,
                rear_wheel__rear_hub__axle_type=frame.axle_type,
                rear_wheel__rear_hub__freehub=cassette.freehub_standard
            )

            serializer = WheelSetSerializer(queryset, many=True)
            return Response(serializer.data, status=200)

        except Frame.DoesNotExist:
            return Response({"error": "Раму не знайдено"}, status=404)
        except Fork.DoesNotExist:
            return Response({"error": "Вилку не знайдено"}, status=404)
        except Cassette.DoesNotExist:
            return Response({"error": "Касету не знайдено"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


class TyreRecommendationAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Отримати сумісні покришки за параметрами",
        manual_parameters=[
            openapi.Parameter('wheel_size', openapi.IN_QUERY, description="Розмір колеса (напр. 29, 700c)",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('max_tyre_width', openapi.IN_QUERY, description="Максимальна ширина покришки",
                              type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request):
        wheel_size = request.GET.get('wheel_size')
        max_tyre_width = request.GET.get('max_tyre_width')

        if not wheel_size or not max_tyre_width:
            return Response({"error": "Потрібні параметри 'wheel_size' і 'max_tyre_width'."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            tyres = Tyre.objects.filter(
                wheel_size__size=wheel_size,
                tyre_size__size__lte=max_tyre_width
            )
            serializer = TyreSerializer(tyres, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StemRecommendationAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Отримати сумісні виноси за параметрами вилки",
        manual_parameters=[
            openapi.Parameter(
                'fork_id',
                openapi.IN_QUERY,
                description="ID вилки",
                type=openapi.TYPE_INTEGER
            ),
        ]
    )
    def get(self, request):
        fork_id = request.GET.get('fork_id')

        if not fork_id:
            return Response({"error": "Потрібно передати 'fork_id'."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            fork = Fork.objects.get(id=fork_id)

            stems = Stem.objects.filter(
                steerer_clamp=fork.stem_diameter
            )

            serializer = StemSerializer(stems, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Fork.DoesNotExist:
            return Response({"error": "Вилка не знайдена."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class HandlebarRecommendationAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Отримати сумісні керма за параметрами виносу",
        manual_parameters=[
            openapi.Parameter(
                'stem_id',
                openapi.IN_QUERY,
                description="ID обраного виносу",
                type=openapi.TYPE_INTEGER
            ),
        ]
    )
    def get(self, request):
        stem_id = request.GET.get('stem_id')

        if not stem_id:
            return Response({"error": "Необхідно передати параметр 'stem_id'."}, status=400)

        try:
            stem = Stem.objects.get(id=stem_id)

            # Пошук керм, які сумісні за діаметром кріплення
            handlebars = Handlebar.objects.filter(stem_clamp=stem.handlebar_clamp)

            serializer = HandlebarSerializer(handlebars, many=True)
            return Response(serializer.data, status=200)

        except Stem.DoesNotExist:
            return Response({"error": "Винос не знайдено."}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


class BrakeRecommendationAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Отримати сумісні гальма за параметрами рами та вилки",
        manual_parameters=[
            openapi.Parameter('frame_id', openapi.IN_QUERY, description="ID рами", type=openapi.TYPE_INTEGER),
            openapi.Parameter('fork_id', openapi.IN_QUERY, description="ID вилки", type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self, request):
        frame_id = request.GET.get('frame_id')
        fork_id = request.GET.get('fork_id')

        if not frame_id or not fork_id:
            return Response({"error": "Потрібно передати 'frame_id' та 'fork_id'."}, status=400)

        try:
            frame = Frame.objects.get(id=frame_id)
            fork = Fork.objects.get(id=fork_id)

            # Пошук гальм, де каліпер сумісний одночасно з кріпленням рами і вилки
            brakes = Brakes.objects.filter(
                caliper__mount__in=[frame.brake_mount, fork.brake_mount]
            ).distinct()

            serializer = BrakeSerializer(brakes, many=True)
            return Response(serializer.data, status=200)

        except Frame.DoesNotExist:
            return Response({"error": "Рама не знайдена"}, status=404)
        except Fork.DoesNotExist:
            return Response({"error": "Вилка не знайдена"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


class BrakeRotorRecommendationAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Підібрати гальмівні ротори за рамою, вилкою та колесами",
        manual_parameters=[
            openapi.Parameter('frame_id', openapi.IN_QUERY, description="ID рами", type=openapi.TYPE_INTEGER),
            openapi.Parameter('fork_id', openapi.IN_QUERY, description="ID вилки", type=openapi.TYPE_INTEGER),
            openapi.Parameter('wheelset_id', openapi.IN_QUERY, description="ID wheelset", type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self, request):
        frame_id = request.GET.get('frame_id')
        fork_id = request.GET.get('fork_id')
        wheelset_id = request.GET.get('wheelset_id')

        if not all([frame_id, fork_id, wheelset_id]):
            return Response({"error": "Необхідно передати frame_id, fork_id та wheelset_id."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            frame = Frame.objects.get(id=frame_id)
            fork = Fork.objects.get(id=fork_id)
            wheelset = WheelSet.objects.get(id=wheelset_id)

            # Мінімально допустимий розмір ротора з рами/вилки
            frame_rotor_diameter = frame.brake_mount.rotor_size.diameter if frame.brake_mount.rotor_size else 0
            fork_rotor_diameter = fork.brake_mount.rotor_size.diameter if fork.brake_mount.rotor_size else 0
            required_diameter = max(frame_rotor_diameter, fork_rotor_diameter)

            # Кріплення ротора з переднього/заднього колеса
            front_mount = wheelset.front_wheel.rotor_mount
            rear_mount = wheelset.rear_wheel.rotor_mount

            # Враховуємо обидва типи кріплення (якщо різні)
            mount_ids = {front_mount.id, rear_mount.id}

            rotors = BrakeRotor.objects.filter(
                mount_id__in=mount_ids,
                diameter__diameter__gte=required_diameter
            ).order_by('diameter__diameter')

            serializer = BrakeRotorSerializer(rotors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Frame.DoesNotExist:
            return Response({"error": "Рама не знайдена."}, status=status.HTTP_404_NOT_FOUND)
        except Fork.DoesNotExist:
            return Response({"error": "Вилка не знайдена."}, status=status.HTTP_404_NOT_FOUND)
        except WheelSet.DoesNotExist:
            return Response({"error": "Wheelset не знайдено."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MTBRecommendationAPIView(APIView):
    def get(self, request, *args, **kwargs):
        bike_id = request.GET.get("bike_id")

        if not bike_id:
            return Response({"error": "Параметр 'bike_id' обов'язковий."}, status=400)

        try:
            target_bike = MTBBike.objects.get(id=bike_id)
        except MTBBike.DoesNotExist:
            return Response({"error": "Велосипед не знайдено."}, status=404)

        bikes = MTBBike.objects.exclude(id=bike_id)

        # Створюємо датафрейм
        data = []
        for bike in bikes:
            data.append({
                "id": bike.id,
                "application": bike.frame.application.id if bike.frame.application else 0,
                "material": bike.frame.material.id if bike.frame.material else 0,
                "brake_type": bike.brake.type if bike.brake else '',
                "weight": float(bike.weight) if bike.weight else 0.0,
                "price": float(bike.price) if bike.price else 0.0,
            })

        df = pd.DataFrame(data)

        if df.empty:
            return Response([], status=200)

        # Об'єкт порівняння
        target_data = {
            "application": target_bike.frame.application.id if target_bike.frame.application else 0,
            "material": target_bike.frame.material.id if target_bike.frame.material else 0,
            "brake_type": target_bike.brake.type if target_bike.brake else '',
            "weight": float(target_bike.weight) if target_bike.weight else 0.0,
            "price": float(target_bike.price) if target_bike.price else 0.0,
        }

        df_full = df.copy()
        df_full["target_application"] = target_data["application"]
        df_full["target_material"] = target_data["material"]
        df_full["target_brake_type"] = target_data["brake_type"]
        df_full["target_weight"] = target_data["weight"]
        df_full["target_price"] = target_data["price"]

        # Нормалізація числових
        scaler = MinMaxScaler()
        numeric = scaler.fit_transform(df_full[["weight", "price", "target_weight", "target_price"]])

        # Категорії – кодуємо вручну
        df_full["application_sim"] = df_full["application"] == df_full["target_application"]
        df_full["material_sim"] = df_full["material"] == df_full["target_material"]
        df_full["brake_type_sim"] = df_full["brake_type"] == df_full["target_brake_type"]

        # Вектор ознак
        feature_matrix = pd.DataFrame(numeric, columns=["weight", "price", "target_weight", "target_price"])
        feature_matrix["application_sim"] = df_full["application_sim"].astype(int)
        feature_matrix["material_sim"] = df_full["material_sim"].astype(int)
        feature_matrix["brake_type_sim"] = df_full["brake_type_sim"].astype(int)

        # Розділити на запит і решту
        query_vector = feature_matrix[["target_weight", "target_price", "application_sim", "material_sim", "brake_type_sim"]].iloc[0].values.reshape(1, -1)
        corpus = feature_matrix[["weight", "price", "application_sim", "material_sim", "brake_type_sim"]].values

        # Подібність
        similarity = cosine_similarity(query_vector, corpus)[0]

        df_full["similarity"] = similarity
        top_ids = df_full.sort_values("similarity", ascending=False)["id"].head(6)

        recommendations = MTBBike.objects.filter(id__in=top_ids)
        serializer = MTBBikeSerializer(recommendations, many=True)
        return Response(serializer.data, status=200)
# class OrderViewSet(ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#     @swagger_auto_schema(operation_summary="List All Orders")
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     @swagger_auto_schema(operation_summary="Retrieve Order Details by ID")
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     @swagger_auto_schema(operation_summary="Create a New Order")
#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#     @swagger_auto_schema(operation_summary="Update an Order")
#     def update(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     @swagger_auto_schema(operation_summary="Delete an Order by ID")
#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)
#
#
# class OrderItemViewSet(ModelViewSet):
#     queryset = OrderItem.objects.all()
#     serializer_class = OrderItemSerializer
#
#     @swagger_auto_schema(operation_summary="List All Ordered Items")
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     @swagger_auto_schema(operation_summary="Retrieve Ordered Item Details by ID")
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     @swagger_auto_schema(operation_summary="Create a New Ordered Item")
#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#     @swagger_auto_schema(operation_summary="Update an Ordered Item")
#     def update(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     @swagger_auto_schema(operation_summary="Delete an Ordered Item by ID")
#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)
