# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 21:58
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_generica'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generica',
            old_name='image',
            new_name='imagen',
        ),
        migrations.RemoveField(
            model_name='generica',
            name='introduction',
        ),
        migrations.AddField(
            model_name='generica',
            name='introduccion',
            field=models.TextField(blank=True, help_text='Texto para describir la página'),
        ),
        migrations.AlterField(
            model_name='generica',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading_block', wagtail.wagtailcore.blocks.StructBlock((('encabezado', wagtail.wagtailcore.blocks.CharBlock(classname='title', required=True)), ('nivel', wagtail.wagtailcore.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))))), ('paragraph_block', wagtail.wagtailcore.blocks.RichTextBlock(icon='fa-paragraph')), ('image_block', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('block_quote', wagtail.wagtailcore.blocks.StructBlock((('texto', wagtail.wagtailcore.blocks.TextBlock()), ('nombre_autor', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='e.g. Guy Picciotto', required=False))))), ('embed_block', wagtail.wagtailembeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15'))), blank=True, verbose_name='Cuerpo de la página'),
        ),
    ]
