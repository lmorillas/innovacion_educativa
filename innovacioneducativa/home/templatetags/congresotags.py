from django import template
from asistentes.models import UsuarioTalleres


register = template.Library()


@register.simple_tag
def participantes():
    return UsuarioTalleres.objects.count()
