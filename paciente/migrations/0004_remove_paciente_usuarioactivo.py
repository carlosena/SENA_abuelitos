# Generated by Django 4.1.2 on 2022-11-08 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_paciente_fechacreacion_paciente_usuarioactivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='usuarioActivo',
        ),
    ]
