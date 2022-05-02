# Generated by Django 4.0.4 on 2022-05-02 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_servicetype_preview_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя пользователя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия пользователя')),
                ('phone', models.CharField(max_length=150, verbose_name='Номер телефона')),
                ('total_price', models.IntegerField(verbose_name='Общая цена')),
            ],
        ),
        migrations.AddField(
            model_name='servicetype',
            name='price_int',
            field=models.IntegerField(default=0, verbose_name='Стоимость услуги'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='OrderService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_service', to='services.order', verbose_name='Заказ')),
                ('service', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='services.servicetype', verbose_name='Заказываемая услуга')),
            ],
        ),
    ]