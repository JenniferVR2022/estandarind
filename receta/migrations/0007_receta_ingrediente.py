# Generated by Django 4.1.1 on 2023-03-21 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingrediente', '0007_alter_ingrediente_estado'),
        ('receta', '0006_receta_estandar'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='ingrediente',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='ingrediente.ingrediente', verbose_name='Ingrediente'),
            preserve_default=False,
        ),
    ]
