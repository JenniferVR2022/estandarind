# Generated by Django 4.1.1 on 2023-06-24 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('email', models.CharField(max_length=50, verbose_name='Correo electrónico')),
                ('tipoDocumento', models.CharField(choices=[('C.C', 'Cédula de Ciudadanía'), ('C.E', 'Cédula de Extranjería'), ('P.A', 'Pasaporte')], default='C.C', max_length=4, verbose_name='Tipo Documento')),
                ('documento', models.CharField(max_length=50, unique=True, verbose_name='Número Documento')),
                ('rol', models.CharField(choices=[('Administrador', 'Administrador'), ('Estandar', 'Estandar'), ('Invitado', 'Invitado')], default='Invitado', max_length=13, verbose_name='Rol')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
