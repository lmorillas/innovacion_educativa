from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

# Create your views here.

from .models import UsuarioTalleres
from .forms import TalleresForm, ListaDeEsperaForm
from home.models import Taller
from django.db.models import Count
from django.db.models import Q
from django.conf import settings

AFORO_MAXIMO = settings.AFORO_MAXIMO
TALLER_MAXIMO = settings.TALLER_MAXIMO


@login_required
def inscripcion(request):
	usuario = UsuarioTalleres.objects.filter(user=request.user)
	if request.method == 'POST':
		if 'cancel' in request.POST:
			redirect('home')
		if usuario:
			form = TalleresForm(request.POST, instance=usuario[0])
		else:
			form = TalleresForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('gracias', permanent=True )
		
	else:
		
		if usuario:
			form = TalleresForm(instance=usuario[0])
		else:
			form = TalleresForm(initial={'user': request.user})
	query = Taller.objects.annotate(taller1T = Count('taller1'),
		taller2T = Count('taller2'),
		taller3T = Count('taller3'),
		taller4T = Count('taller4'),
		)

	#q1 = Q(taller1T__lt=0 ) | Q(nombre=form.instance.taller1) if form.instance.taller else Q(taller1T__lt=1 )
	form.fields['taller1'].queryset = query.filter( Q(taller1T__lt=TALLER_MAXIMO ) | Q(nombre=form.instance.taller1) )
	form.fields['taller2'].queryset = query.filter( Q(taller2T__lt=TALLER_MAXIMO ) | Q(nombre=form.instance.taller2) )
	form.fields['taller3'].queryset = query.filter( Q(taller3T__lt=TALLER_MAXIMO ) | Q(nombre=form.instance.taller3) )
	form.fields['taller4'].queryset = query.filter( Q(taller4T__lt=TALLER_MAXIMO ) | Q(nombre=form.instance.taller4) )
	context = {'form': form }
	return render(request, 'asistentes/talleres.html', context)

@login_required
def incripcion_update(request, pk, template_name='asistentes/talleres.html'):
	datos = get_object_or_404(UsuarioTalleres, user=request.user)
	form = TalleresForm(request.POST or None, instance=datos)
	if form.is_valid():
		form.save()
		return redirect('home')
	return render(request, template_name, {'form':form})

@login_required
def gracias(request, template_name='asistentes/gracias.html'):
	contexto = {'usuario': request.user.username}
	logout(request)
	return render(request, template_name, contexto)


@login_required
def lista_espera(request):
	if request.method == 'POST':
		form = Lista(request.POST)
		if form.is_valid():
			form.save()
			return redirect('gracias', permanent=True )
		
	else:
		
		if usuario:
			form = TalleresForm(instance=usuario[0])
		else:
			form = TalleresForm(initial={'user': request.user})
	query = Taller.objects.annotate(taller1T = Count('taller1'),
		taller2T = Count('taller2'),
		taller3T = Count('taller3'),
		taller4T = Count('taller4'),
		)

	#q1 = Q(taller1T__lt=0 ) | Q(nombre=form.instance.taller1) if form.instance.taller else Q(taller1T__lt=1 )
	form.fields['taller1'].queryset = query.filter( Q(taller1T__lt=TALLER_MAXIMO ) | Q(nombre=form.instance.taller1) )
	form.fields['taller2'].queryset = query.filter( Q(taller2T__lt=TALLER_MAXIMO ) | Q(nombre=form.instance.taller2) )
	form.fields['taller3'].queryset = query.filter( Q(taller3T__lt=TALLER_MAXIMO ) | Q(nombre=form.instance.taller3) )
	form.fields['taller4'].queryset = query.filter( Q(taller4T__lt=TALLER_MAXIMO ) | Q(nombre=form.instance.taller4) )
	context = {'form': form }
	return render(request, 'asistentes/talleres.html', context)