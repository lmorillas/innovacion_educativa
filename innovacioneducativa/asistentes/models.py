from django.db import models
from django.contrib.auth.models import AbstractUser
from home.models import Taller
from django.contrib.auth.models import User


class UsuarioTalleres(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(verbose_name='Nombre', max_length=120)
    apellidos = models.CharField(verbose_name='Apellidos', max_length=240)
    nif = models.CharField(verbose_name='NIF', max_length=32)
    activo = models.BooleanField(verbose_name="¿Eres profesor/a en activo?", default=False)
    signos = models.BooleanField(verbose_name="¿Necesitas intérprete de lengua de signos?", default=False)
    traduccion = models.BooleanField(verbose_name="¿Necesitas traducción simultánea?", default=False)
    centro_educativo = models.CharField(verbose_name='Centro Educativo', max_length=256,
    	null=True, blank=True)
    comunidad_autonoma = models.CharField(verbose_name='Comunidad Autónoma', max_length=256,
    	null=True, blank=True)
    taller1 = models.ForeignKey(Taller, verbose_name="Viernes 1", on_delete=models.SET_NULL, null=True, 
    	blank = True, related_name = 'taller1', related_query_name="taller1")
    taller2 = models.ForeignKey(Taller, verbose_name="Viernes 2", on_delete=models.SET_NULL, null=True,
    	 blank = True, related_name='taller2', related_query_name="taller2")
    taller3 = models.ForeignKey(Taller, verbose_name="Viernes 3", on_delete=models.SET_NULL, null=True, 
    	 blank = True, related_name='taller3', related_query_name="taller3")
    taller4 = models.ForeignKey(Taller, verbose_name="Sábado", on_delete=models.SET_NULL, null=True,
    	 blank = True, related_name='taller4', related_query_name="taller4")

class ListaDeEspera(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nombre = models.CharField(verbose_name='Nombre', max_length=120)
	apellidos = models.CharField(verbose_name='Apellidos', max_length=240)
	nif = models.CharField(verbose_name='NIF', max_length=32)
	activo = models.BooleanField(verbose_name="¿Eres profesor/a en activo?", default=False)
	signos = models.BooleanField(verbose_name="¿Necesitas intérprete de lengua de signos?", default=False)
	traduccion = models.BooleanField(verbose_name="¿Necesitas traducción simultánea?", default=False)
	centro_educativo = models.CharField(verbose_name='Centro Educativo', max_length=256,
		null=True, blank=True)
	comunidad_autonoma = models.CharField(verbose_name='Comunidad Autónoma', max_length=256,
		null=True, blank=True)
