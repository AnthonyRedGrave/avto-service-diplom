from django.contrib import admin
from django import forms

from .models import ServiceSuggestion, ServiceType
from ckeditor.widgets import CKEditorWidget


class ServiceTypeAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = ServiceType
        fields = '__all__'


class ServiceTypeAdmin(admin.ModelAdmin):
    form = ServiceTypeAdminForm


admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(ServiceSuggestion)