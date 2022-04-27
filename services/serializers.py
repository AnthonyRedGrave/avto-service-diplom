from rest_framework import serializers
from .models import ServiceType


class ServiceTypeSerializer(serializers.ModelSerializer):
    suggestions = serializers.StringRelatedField(many=True)
    class Meta:
        model = ServiceType
        fields = ['id', 'title', 'contacts', 'time', 'price', 'warranty', 'text', 'suggestions', 'get_type_display']
