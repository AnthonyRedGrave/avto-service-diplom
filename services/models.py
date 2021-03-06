from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()


class ServiceSuggestion(models.Model):
    title = models.CharField("Предложение", max_length=150)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Предложение услуги'
        verbose_name_plural = 'Предложения услуги'


class ServicePhoto(models.Model):
    title = models.CharField("Название", max_length=150)
    image = models.FileField("Изображение для услуги", upload_to="services/images/")
    gallery = models.ForeignKey('ServiceGallery', related_name='images', on_delete=models.CASCADE, verbose_name='Галерея')

    def __str__(self) -> str:
        return f"Изображение для {self.gallery}"

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class ServiceGallery(models.Model):
    service = models.OneToOneField('ServiceType', related_name='gallery', on_delete=models.CASCADE, verbose_name='Услуга')

    def __str__(self) -> str:
        return f"Галерея для услуги {self.service.title}"

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class ServiceType(models.Model):
    class ServiceTypeChoice(models.TextChoices):
        repair = "repair", "Ремонт"
        service = "service", "Услуги"
        electric = "electric", "Автоэлектрика"

    title = models.CharField("Название услуги", max_length=150)
    contacts = models.ManyToManyField(User)
    time = models.CharField("Время услуги", max_length=30)
    price = models.CharField("Стоимость услуги за полный цикл", max_length=30)
    price_int = models.IntegerField("Стоимость услуги")
    warranty = models.CharField("Гарантия", max_length=50)
    text = models.TextField("Информация об услуге")
    suggestions = models.ManyToManyField(ServiceSuggestion, verbose_name="Предложения")
    type = models.CharField("Тип услуги", max_length=60, choices=ServiceTypeChoice.choices)
    preview_text = models.TextField('Текст для превью', null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Тип услуги'
        verbose_name_plural = 'Типы услуг'


@receiver(post_save, sender=ServiceType)
def create_service_gallery(sender, instance, **kwargs):
    gallery, created = ServiceGallery.objects.get_or_create(service=instance)


class OrderService(models.Model):
    service = models.ForeignKey(ServiceType, verbose_name='Заказываемая услуга', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', related_name='ordered_service', on_delete=models.CASCADE, verbose_name='Заказ')

    def __str__(self) -> str:
        return f"Заказанная услуга {self.service.title} - {self.order.phone}"

    class Meta:
        verbose_name = 'Заказываемая услуга'
        verbose_name_plural = 'Заказываемые услуги'




class Order(models.Model):
    first_name = models.CharField("Имя пользователя", max_length=150)
    last_name = models.CharField("Фамилия пользователя", max_length=150)
    phone = models.CharField("Номер телефона", max_length=150)
    total_price = models.IntegerField("Общая цена", default=0)

    def __str__(self) -> str:
        return f"Заказ {self.first_name} - {self.last_name} - {self.phone} - {self.total_price}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
