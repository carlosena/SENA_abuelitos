# Generated by Django 4.1.2 on 2022-10-31 00:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamento', '0015_alter_medicamento_ultimadosis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='ultimaDosis',
            field=models.DateField(default=datetime.datetime.now, null=True, verbose_name='Hora última dosis'),
        ),
    ]