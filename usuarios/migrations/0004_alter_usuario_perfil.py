# Generated by Django 4.1.2 on 2022-10-24 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_usuario_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='perfil',
            field=models.CharField(choices=[('admin', 'Administrador'), ('user', 'Usuario')], default='user', max_length=5, null=True, verbose_name='Perfil'),
        ),
    ]
