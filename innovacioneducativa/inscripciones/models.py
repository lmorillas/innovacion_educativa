from django.db import models
from django.contrib.auth.models import AbstractUser

from home.models import Taller


# Create your models here.
class Participante(AbstractUser):

	country = models.CharField(verbose_name='country', max_length=255, blank=True)
	#status = models.ForeignKey(Taller, on_delete=models.SET_NULL, null=True, default=1)

