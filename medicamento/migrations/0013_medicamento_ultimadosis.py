# Generated by Django 4.1.2 on 2022-10-31 00:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamento', '0012_alter_medicamento_fechadosis'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='ultimaDosis',
            field=models.DateField(default=datetime.date.today, null=True, verbose_name='Hora última dosis'),
        ),
    ]
