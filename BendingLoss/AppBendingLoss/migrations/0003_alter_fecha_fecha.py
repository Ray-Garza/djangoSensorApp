# Generated by Django 4.2.2 on 2023-07-05 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppBendingLoss", "0002_remove_sensor_esinicial_sensor_indice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fecha",
            name="fecha",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
