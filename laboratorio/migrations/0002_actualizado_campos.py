# Generated by Django 5.1.2 on 2024-11-06 09:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='directorgeneral',
            name='especialidad',
            field=models.CharField(default='No especificado', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='ciudad',
            field=models.CharField(default='No especificado', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='pais',
            field=models.CharField(default='No especificado', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='f_fabricacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
