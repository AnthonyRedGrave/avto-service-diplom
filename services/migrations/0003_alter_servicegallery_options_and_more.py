# Generated by Django 4.0.4 on 2022-04-28 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_servicegallery_servicephoto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicegallery',
            options={'verbose_name': 'Галерея', 'verbose_name_plural': 'Галереи'},
        ),
        migrations.AlterModelOptions(
            name='servicephoto',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
    ]
