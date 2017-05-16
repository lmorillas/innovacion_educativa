# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 06:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('home', '0029_auto_20170511_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='pildoras',
            name='imagen_pildora',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]