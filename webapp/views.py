# Create your views here.
# myapp/views.py
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .models import Case, Order, OrderItem
from .serializers import MTBBikeSerializer, RoadBikeSerializer, \
    FrameSerializer, ForkSerializer, WheelSetSerializer, CranksetSerializer  # , OrderSerializer, OrderItemSerializer
from .models import MTBBike, RoadBike, Frame, Fork, WheelSet, Crankset
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
        operation_summary="Get recommended cranksets by chainline and gearing",
        manual_parameters=[
            openapi.Parameter('chainline', openapi.IN_QUERY, description="Required chainline in mm",
                              type=openapi.TYPE_NUMBER),
            openapi.Parameter('gearing', openapi.IN_QUERY, description="Number of gears (e.g., 12 for 1x12)",
                              type=openapi.TYPE_INTEGER)
        ]
    )
    def get(self, request):
        try:
            chainline = request.GET.get('chainline')
            gearing = request.GET.get('gearing')

            if not chainline or not gearing:
                return Response({"error": "Missing required parameters."}, status=status.HTTP_400_BAD_REQUEST)

            chainline = float(chainline)
            gearing = int(gearing)

            cranksets = Crankset.objects.filter(
                gearing=gearing,
                chainline__gte=chainline - 2,
                chainline__lte=chainline + 2
            )

            serializer = CranksetSerializer(cranksets, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ValueError:
            return Response({"error": "Invalid input values."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WheelSetRecommendationAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Підібрати сумісний WheelSet за рамою та вилкою",
        manual_parameters=[
            openapi.Parameter('frame_id', openapi.IN_QUERY, description="ID рами", type=openapi.TYPE_INTEGER),
            openapi.Parameter('fork_id', openapi.IN_QUERY, description="ID вилки", type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self, request):
        frame_id = request.GET.get('frame_id')
        fork_id = request.GET.get('fork_id')

        if not frame_id or not fork_id:
            return Response({"error": "Потрібно передати frame_id та fork_id"}, status=400)

        try:
            frame = Frame.objects.get(id=frame_id)
            fork = Fork.objects.get(id=fork_id)

            queryset = WheelSet.objects.filter(
                wheel_size=frame.wheel_size,
                front_wheel__front_hub__axle_type=fork.axle_type,
                rear_wheel__rear_hub__axle_type=frame.axle_type
            )

            serializer = WheelSetSerializer(queryset, many=True)
            return Response(serializer.data, status=200)

        except Frame.DoesNotExist:
            return Response({"error": "Рама не знайдена"}, status=404)
        except Fork.DoesNotExist:
            return Response({"error": "Вилка не знайдена"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
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
