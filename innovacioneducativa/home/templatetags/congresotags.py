from django import template
from asistentes.models import UsuarioTalleres



register = template.Library()


@register.simple_tag
def participantes():
	'''
	Devuelve número de asistentes que han confirmado ya el email y se han inscrito
	'''
	return UsuarioTalleres.objects.count()
