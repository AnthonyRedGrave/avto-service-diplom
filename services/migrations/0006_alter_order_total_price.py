# Generated by Django 4.0.4 on 2022-05-02 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_order_servicetype_price_int_orderservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=0, verbose_name='Общая цена'),
        ),
    ]
