from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Order, OrderService, ServiceType
from .serializers import ServiceTypeSerializer, OrderSerializer


class ServiceTypeViewset(ModelViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        type = self.request.query_params.get('type')
        if type:
            queryset = queryset.filter(type=type)
        return queryset


class OrderServiceViewSet(mixins.CreateModelMixin, ReadOnlyModelViewSet):
    queryset = OrderService.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=["post"])
    def make_order(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = Order.objects.create(first_name=serializer.validated_data['first_name'],
                                     last_name=serializer.validated_data['last_name'],
                                     phone=serializer.validated_data['phone'])
        
        total_price = 0
        for order_service in serializer.validated_data['orders']:
            OrderService.objects.create(service=order_service, order=order)
            total_price += order_service.price_int
        order.total_price = total_price
        order.save()
        return Response({"Created!"})