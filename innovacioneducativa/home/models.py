# coding: utf-8

from __future__ import absolute_import, unicode_literals

from django.db import models
from django.shortcuts import render, redirect

from wagtail.wagtailcore.models import Page, Orderable


from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel
from wagtail.wagtailcore.blocks import RawHTMLBlock, RichTextBlock, StreamBlock, CharBlock
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from modelcluster.fields import ParentalKey
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route


from django.utils.encoding import python_2_unicode_compatible
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from .blocks import BaseStreamBlock

from django.contrib.auth.models import User

from django.conf import settings
from asistentes.models import Participante


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
    lema =  models.CharField(max_length=240, blank = True) 
    presentacion = StreamField(HTMLBlock(), blank=True)
    objetivos = StreamField(HTMLBlock(), blank=True)
    titulo_consejera = models.CharField(max_length=240, blank = True) 
    saludo_consejera = StreamField(HTMLBlock(), blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('titulo'),
        FieldPanel('lema'),
        FieldPanel('subtitulo'),
        ImageChooserPanel("imagen_principal"),
        StreamFieldPanel("presentacion"),
        StreamFieldPanel("objetivos"),
        ImageChooserPanel("imagen_consejera"),
        FieldPanel('titulo_consejera'),
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

    def serve(self, request):
        from home.forms import PreguntaMesaForm

        if request.method == 'POST':
            form = PreguntaMesaForm(request.POST)
            if form.is_valid():
                pregunta = form.save()

            return redirect('/preguntas-la-mesa-redonda/gracias')
        else:
            form = PreguntaMesaForm()

            return render(request, 'home/ponentes.html', {
                'page': self,
                'form': form,
                })

    
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
    mensaje_inscripciones = RichTextField(help_text='Mensaje inscripciones', 
        null=True, blank=True)
    contenido = RichTextField(help_text='Texto inscripciones')

    def get_context(self, request):
        context = super(PaginaInscripciones, self).get_context(request)

        # Add extra variables and return the updated context
        num_inscripciones = Participante.objects.count()  
        #UsuarioTalleres.objects.count()
        context['num_inscripciones'] = num_inscripciones
        context['completo'] = num_inscripciones >= settings.AFORO_MAXIMO
        return context
        
    content_panels = Page.content_panels + [
        FieldPanel('mensaje_inscripciones', classname="full"),
        FieldPanel('contenido', classname="full"),
        ]

class PreguntaMesa(Orderable):
    
    page = ParentalKey('PaginaPreguntasMesa', related_name='preguntas', null=True)
    pregunta = models.CharField("Pregunta a la mesa", max_length=255)
    quien = models.CharField("¿Quién eres?", max_length=255)
    validada = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        p = PaginaPreguntasMesa.objects.get()
        self.page = p
        super(PreguntaMesa, self).save(*args, **kwargs) # Call the "real" save() method.

class PaginaPreguntasMesa(RoutablePageMixin, Page):
    body = RichTextField(blank=True)
    thanks = RichTextField('Mensaje agradecimiento', blank=True)

    def validadas(self):
        return self.preguntas.filter(validada=True)

    @route(r'^gracias/$')
    def gracias(self, request):
        context = self.get_context(request)
        context['gracias'] = 'gracias'
        
        return render(request, 'home/pagina_preguntas_mesa.html', context)

PaginaPreguntasMesa.content_panels = Page.content_panels + [
    FieldPanel('body', classname="full"),
    FieldPanel('thanks', classname="full"),
    InlinePanel('preguntas', label="Pregunta"),
    ]
    


class Pildora(Orderable):
    
    page = ParentalKey('Pildoras', related_name='pildoras')
    nombre = models.CharField("Nombre del micro-taller", max_length=255)
    quien = RichTextField("Coordinador", blank=True, null=True)
    procedencia = RichTextField("Centro", blank=True, null=True)
    observaciones = RichTextField("Observaciones", blank=True, null=True)
    email =RichTextField("email", blank=True, null=True)

    panels = [
        FieldPanel('nombre'),
        FieldPanel('quien'),
        FieldPanel('procedencia'),
        FieldPanel('email'),
        FieldPanel('observaciones'),
    ]
    def __str__(self):
        return "{}".format(self.nombre)
       

class Pildoras(Page):
    body = RichTextField(blank=True)
    imagen_pildora = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    
Pildoras.content_panels = Page.content_panels + [
    FieldPanel('body', classname="full"),
    ImageChooserPanel("imagen_pildora"),
    InlinePanel('pildoras', label="Píldoras"),
    ]



import django_tables2 as tables
from django_tables2 import RequestConfig


class InscritosTable(tables.Table):
    class Meta:
        model = Participante
        # add class="paleblue" to <table> tag
        attrs = {'class': 'table table-bordered'}


class ListaInscritos(Page):
    body = RichTextField(blank=True)
    
    def get_context(self, request):
        from asistentes.models import Participante

        context = super(ListaInscritos, self).get_context(request)

        inscritos = InscritosTable(Participante.objects.all())
        RequestConfig(request, paginate={'per_page': 25}).configure(inscritos)

        context['inscritos'] = inscritos
        return context


    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        ]


class PaginaEstandar(Page):
    """
    A generic content page. On this demo site we use it for an about page but
    it could be used for any type of page content that only needs a title,
    image, introduction and body field
    """

    introduction = models.TextField(verbose_name="Introducción",
        help_text='Texto para describir la página',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name = "Imagen principal",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Imagen principal. Sólo horizontal. Anchura entre 1000px y 3000px.'
    )
    body = StreamField(
        BaseStreamBlock(), verbose_name="Cuerpo de la página", blank=True
    )
    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        StreamFieldPanel('body'),
        ImageChooserPanel('image'),
    ]



