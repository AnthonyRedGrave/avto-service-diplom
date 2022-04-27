from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ServiceType
from .serializers import ServiceTypeSerializer


class ServiceTypeViewset(ModelViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        type = self.request.query_params.get('type')
        if type:
            queryset = queryset.filter(type=type)
        return queryset
