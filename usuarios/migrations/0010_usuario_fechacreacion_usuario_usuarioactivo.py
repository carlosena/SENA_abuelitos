# Generated by Django 4.1.2 on 2022-11-08 00:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_usuario_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='fechaCreacion',
            field=models.DateField(default=datetime.date.today, null=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='usuarioActivo',
            field=models.CharField(max_length=20, null=True, verbose_name='Usuario activo'),
        ),
    ]
