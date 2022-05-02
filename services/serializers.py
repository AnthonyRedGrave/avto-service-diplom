from django.forms import ValidationError
from rest_framework import serializers
from contacts.serializers import UserSerializer
from .models import ServiceType, Order


class ServiceTypeSerializer(serializers.ModelSerializer):
    suggestions = serializers.StringRelatedField(many=True)
    contacts = UserSerializer(many=True)
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        return obj.gallery.images.all().values_list('image', flat=True)
    
    class Meta:
        model = ServiceType
        fields = ['id', 'title', 'contacts', 'time', 'price', 'warranty', 'text', 'suggestions', 'get_type_display', 'images', 'preview_text', 'price_int']


class OrderSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone = serializers.CharField()
    orders = serializers.ListField()

    def validate_orders(self, value):
        orders_from_db = ServiceType.objects.filter(id__in=value).all()
        if orders_from_db.count() != len(value):
            raise ValidationError("Не все услуги существуют!")
        return orders_from_db

    