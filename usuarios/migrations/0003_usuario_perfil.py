# Generated by Django 4.1.2 on 2022-10-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='perfil',
            field=models.CharField(choices=[('1', 'Administrador'), ('0', 'Usuario')], default='0', max_length=1, null=True, verbose_name='Perfil'),
        ),
    ]