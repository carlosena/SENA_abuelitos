# Generated by Django 4.1.2 on 2022-10-24 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicamento', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicamento',
            name='cantidad',
        ),
    ]
