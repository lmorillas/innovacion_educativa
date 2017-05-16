# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 06:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20170317_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='doscolumnas',
            name='titulocol1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='doscolumnas',
            name='titulocol2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='taller',
            name='imagen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]