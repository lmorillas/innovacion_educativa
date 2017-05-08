# coding: utf-8

from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page, Orderable


from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel
from wagtail.wagtailcore.blocks import RawHTMLBlock, RichTextBlock, StreamBlock, CharBlock
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from modelcluster.fields import ParentalKey

from django.utils.encoding import python_2_unicode_compatible
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from .blocks import BaseStreamBlock

MAX_TALLER=25

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
    titulo = models.CharField(max_length=240, 
        default="I Jornadas de INNOVACIÓN METODOLÓGICA EN EDUCACIÓN")
    subtitulo = models.CharField(max_length=200, 
        default= "22-23 Septiembre - Zaragoza")
    presentacion = StreamField(HTMLBlock(), blank=True)
    objetivos = StreamField(HTMLBlock(), blank=True)
    saludo_consejera = StreamField(HTMLBlock(), blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('titulo'),
        FieldPanel('subtitulo'),
        ImageChooserPanel("imagen_principal"),
        StreamFieldPanel("presentacion"),
        StreamFieldPanel("objetivos"),
        ImageChooserPanel("imagen_consejera"),
        StreamFieldPanel("saludo_consejera"),
    ]

class DosColumnas(Page):
    titulo = models.CharField(max_length=200)
    titulocol1 = models.CharField(max_length=200, blank=True)
    titulocol2 = models.CharField(max_length=200, blank=True)
    columna1 = RichTextField(blank=True)
    columna2 = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('titulo'),
        FieldPanel('titulocol1'),
        FieldPanel('columna1'),
        FieldPanel('titulocol2'),
        FieldPanel('columna2'),
        
    ]


class Personal(Orderable):
    
    nombre = models.CharField("Nombre", max_length=255)
    imagen = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    biografia = RichTextField(blank=True)
    descripcion = RichTextField(blank=True)
    mas_info = models.URLField("URL mas info", blank=True)

    panels = [
        FieldPanel('nombre'),
        FieldPanel('biografia'),
        FieldPanel('descripcion'),
        FieldPanel('mas_info'),

        ImageChooserPanel('imagen'),
    ]
    class Meta:
        abstract = True


class Ponente(Personal):
    page = ParentalKey('Ponentes', related_name='ponentes')

class Mesa(Personal):
    page = ParentalKey('Ponentes', related_name='coordinador')

class Ponentes(Page):
    body = RichTextField(blank=True)
    
Ponentes.content_panels = Page.content_panels + [
    FieldPanel('body', classname="full"),
    InlinePanel('ponentes', label="Ponente"),
    InlinePanel('coordinador', label="Coordinador mesa", max_num=1),
    ]


# Snippets para encabezado y pie
@register_snippet
@python_2_unicode_compatible  # provide equivalent __unicode__ and __str__ methods on Python 2
class Encabezado_y_Pie(models.Model):
    logo_caixa = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    logo_dga = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    panels = [
        ImageChooserPanel('logo_caixa'),
        ImageChooserPanel('logo_dga'),
    ]


class Taller(Orderable):
    
    page = ParentalKey('Talleres', related_name='talleres')
    nombre = models.CharField("Nombre del taller", max_length=255)
    imagen = models.CharField("Imagen", max_length=255, blank=True, null=True)
    coordinador = RichTextField(blank=True)
    biografia = RichTextField(blank=True)
    descripcion = RichTextField(blank=True)
    mas_info =RichTextField(blank=True)

    panels = [
        FieldPanel('nombre'),
        FieldPanel('imagen'),
        FieldPanel('coordinador'),
        FieldPanel('descripcion'),
        FieldPanel('mas_info'),
    ]
    def __str__(self):
        return "{}".format(self.nombre)
       


class Talleres(Page):
    body = RichTextField(blank=True)
    
Talleres.content_panels = Page.content_panels + [
    FieldPanel('body', classname="full"),
    InlinePanel('talleres', label="Taller"),
    ]


class Comunicaciones(Page):
    body = RichTextField(blank=True)

    template = 'comunicaciones.html'
    
Comunicaciones.content_panels = Page.content_panels + [
    FieldPanel('body', classname="full"),
    ]

class Contacto(Page):
    body = RichTextField(blank=True)
    template = 'contacto.html'
    
Contacto.content_panels = Page.content_panels + [
    FieldPanel('body', classname="full"),
    ]


class Generica(Page):
    """
    Página genérica 
    """

    introduccion = models.TextField(
        help_text='Texto para describir la página',
        blank=True)
    imagen = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )
    body = StreamField(
        BaseStreamBlock(), verbose_name="Cuerpo de la página", blank=True
    )
    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full"),
        StreamFieldPanel('body'),
        ImageChooserPanel('imagen'),
    ]


class PaginaPresentacion(Page):
    """
    Página de presentacion 
    """
    presentacion = RichTextField(help_text='Texto presentación')
    objetivos = RichTextField(help_text='Texto objetivos')

    content_panels = Page.content_panels + [
        FieldPanel('presentacion', classname="full"),
        FieldPanel('objetivos', classname="full")
        ]

class PaginaInscripciones(Page):
    """
    Página de inscripciones 
    """
    contenido = RichTextField(help_text='Texto inscripciones')
    

    content_panels = Page.content_panels + [
        FieldPanel('contenido', classname="full"),
        ]

class Pregunta(Orderable):
    
    page = ParentalKey('PaginaPregunasMesa', related_name='preguntas')
    pregunta = models.CharField("Pregunta a la mesa", max_length=255)
    quien = models.CharField("Quién pregunta?", max_length=255)
    validada = models.BooleanField(default=False)

    panels = [
        FieldPanel('pregunta'),
        FieldPanel('quien'),
        FieldPanel('validadad')
        ]
