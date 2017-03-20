from django.db import models
from django.contrib.auth.models import AbstractUser

from home.models import Taller


# Create your models here.
class Participante(AbstractUser):

	situacion_laboral = models.CharField(verbose_name='Situación laboral', max_length=255, blank=True)
	centro_educativo = models.CharField(verbose_name='Centro Educativo', max_length=255, blank=True)
	comunidad_autónoma = models.CharField(verbose_name='Comunidad Autónoma', max_length=255, blank=True)
	taller1 = models.ForeignKey(Taller, on_delete=models.CASCADE, blank=True, 
		verbose_name="taller 1", related_name="taller1")
	taller2 = models.ForeignKey(Taller, on_delete=models.CASCADE, blank=True, 
		verbose_name="taller 2", related_name="taller2")
	taller3 = models.ForeignKey(Taller, on_delete=models.CASCADE, blank=True, 
		verbose_name="taller 3", related_name="taller3")
	taller4 = models.ForeignKey(Taller, on_delete=models.CASCADE, blank=True, 
		verbose_name="taller 4", related_name="taller4")

