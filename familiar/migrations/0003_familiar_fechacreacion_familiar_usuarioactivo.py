# Generated by Django 4.1.2 on 2022-11-08 01:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiar', '0002_alter_familiar_numdocumento'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='fechaCreacion',
            field=models.DateField(default=datetime.date.today, null=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AddField(
            model_name='familiar',
            name='usuarioActivo',
            field=models.CharField(default='admin', max_length=15),
        ),
    ]
