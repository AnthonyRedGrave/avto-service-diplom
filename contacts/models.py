from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField("Номер", max_length=50, default="+37533123456")
    working_mode = models.CharField("Режим работы", max_length=50, null=True, default="Понедельник - воскресенье 8:00 - 21:00")