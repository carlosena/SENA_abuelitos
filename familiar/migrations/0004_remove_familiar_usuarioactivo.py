# Generated by Django 4.1.2 on 2022-11-08 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familiar', '0003_familiar_fechacreacion_familiar_usuarioactivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiar',
            name='usuarioActivo',
        ),
    ]
