# Generated by Django 4.0.1 on 2022-02-02 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscaTuMascota', '0007_alter_mascota_qr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='qr',
            field=models.BinaryField(),
        ),
    ]
