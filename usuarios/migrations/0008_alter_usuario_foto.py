# Generated by Django 4.1.2 on 2022-11-04 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_usuario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, default='images/default.png', upload_to='images/'),
        ),
    ]