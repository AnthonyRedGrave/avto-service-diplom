from rest_framework import serializers
from contacts.serializers import UserSerializer
from .models import ServiceType


class ServiceTypeSerializer(serializers.ModelSerializer):
    suggestions = serializers.StringRelatedField(many=True)
    contacts = UserSerializer(many=True)
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        return obj.gallery.images.all().values_list('image', flat=True)
    
    class Meta:
        model = ServiceType
        fields = ['id', 'title', 'contacts', 'time', 'price', 'warranty', 'text', 'suggestions', 'get_type_display', 'images']
