# Generated by Django 4.2.17 on 2024-12-09 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baykeshoporders',
            name='is_verify',
            field=models.BooleanField(default=False, verbose_name='核销订单'),
        ),
    ]
