# Generated by Django 5.1.6 on 2025-03-03 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='position',
            field=models.FloatField(unique=True),
        ),
    ]
