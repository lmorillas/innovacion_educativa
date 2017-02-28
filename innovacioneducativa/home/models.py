from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page


from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.blocks import RawHTMLBlock, RichTextBlock, StreamBlock
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page


class HTMLBlock(StreamBlock):
    raw_html = RawHTMLBlock()
    rich_text = RichTextBlock()


class HTMLPage(Page):
    """General page model containing blocks of HTML content."""
    content = StreamField(HTMLBlock())

    content_panels = Page.content_panels + [StreamFieldPanel("content"), ]


class HomePage(Page):
    imagen_principal = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    imagen_consejera = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    presentacion = StreamField(HTMLBlock(), blank=True)
    objetivos = StreamField(HTMLBlock(), blank=True)
    saludo_consejera = StreamField(HTMLBlock(), blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("imagen_principal"),
        StreamFieldPanel("presentacion"),
        StreamFieldPanel("objetivos"),
        FieldPanel("imagen_consejera"),
        StreamFieldPanel("saludo_consejera")
    ]

