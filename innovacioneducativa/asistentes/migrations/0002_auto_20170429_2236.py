# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-29 20:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asistentes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariotalleres',
            name='taller1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taller1', to='home.Taller'),
        ),
        migrations.AlterField(
            model_name='usuariotalleres',
            name='taller2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taller2', to='home.Taller'),
        ),
        migrations.AlterField(
            model_name='usuariotalleres',
            name='taller3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taller3', to='home.Taller'),
        ),
        migrations.AlterField(
            model_name='usuariotalleres',
            name='taller4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taller4', to='home.Taller'),
        ),
    ]