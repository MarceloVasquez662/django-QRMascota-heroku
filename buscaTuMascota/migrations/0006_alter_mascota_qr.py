# Generated by Django 4.0.1 on 2022-02-01 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscaTuMascota', '0005_mascota_qr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='qr',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
