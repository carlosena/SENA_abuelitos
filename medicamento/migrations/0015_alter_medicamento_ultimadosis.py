# Generated by Django 4.1.2 on 2022-10-31 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamento', '0014_alter_medicamento_ultimadosis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='ultimaDosis',
            field=models.DateField(auto_now=True, null=True, verbose_name='Hora última dosis'),
        ),
    ]
