# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyCar', '0002_auto_20171218_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auto',
            name='id_color',
        ),
        migrations.RemoveField(
            model_name='auto',
            name='id_mark',
        ),
        migrations.RemoveField(
            model_name='rent',
            name='id_auto',
        ),
        migrations.AddField(
            model_name='rent',
            name='id_model',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='MyCar.ModelCar', verbose_name='Автомобиль'),
        ),
        migrations.DeleteModel(
            name='Auto',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
    ]
