from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ServiceSuggestion(models.Model):
    title = models.CharField("Предложение", max_length=150)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Предложение услуги'
        verbose_name_plural = 'Предложения услуги'


class ServiceType(models.Model):
    class ServiceTypeChoice(models.TextChoices):
        repair = "repair", "Ремонт"
        service = "service", "Услуги"
        electric = "electric", "Автоэлектрика"

    title = models.CharField("Название услуги", max_length=150)
    contacts = models.ManyToManyField(User)
    time = models.CharField("Время услуги", max_length=30)
    price = models.CharField("Стоимость услуги за полный цикл", max_length=30)
    warranty = models.CharField("Гарантия", max_length=50)
    text = models.TextField("Информация об услуге")
    suggestions = models.ManyToManyField(ServiceSuggestion, verbose_name="Предложения")
    type = models.CharField("Тип услуги", max_length=60, choices=ServiceTypeChoice.choices)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Тип услуги'
        verbose_name_plural = 'Типы услуг'
