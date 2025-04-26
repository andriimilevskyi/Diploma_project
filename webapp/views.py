# Create your views here.
# myapp/views.py
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet
# from .models import Case, Order, OrderItem
from .serializers import MTBBikeSerializer, RoadBikeSerializer  # , OrderSerializer, OrderItemSerializer
from .models import MTBBike, RoadBike

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
