# Generated by Django 4.1.2 on 2022-10-26 15:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamento', '0002_remove_medicamento_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='consumoDiario',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Consumo Diario'),
        ),
    ]
