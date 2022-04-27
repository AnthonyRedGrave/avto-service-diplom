from tkinter import E
from django.contrib import admin
from django import forms

from .models import ServiceGallery, ServicePhoto, ServiceSuggestion, ServiceType
from ckeditor.widgets import CKEditorWidget




class ServiceTypeAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = ServiceType
        fields = '__all__'


class ServiceTypeAdmin(admin.ModelAdmin):
    form = ServiceTypeAdminForm
    list_display=(
        "title",
        "price",
        "type",
        "warranty",
        "time"
    )


admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(ServiceSuggestion)
admin.site.register(ServiceGallery)
admin.site.register(ServicePhoto)