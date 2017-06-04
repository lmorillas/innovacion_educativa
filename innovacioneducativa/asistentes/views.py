from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

import csv
from django.http import StreamingHttpResponse, HttpResponse
from django.utils.encoding import smart_str
from django.utils.translation import ugettext as _

# Create your views here.

from .forms import EmailForm, AsistenteForm, EsperaForm
from home.models import Taller
from django.db.models import Count
from django.db.models import Q
from django.conf import settings

from .models import Participante, ListaDeEspera

from io import StringIO

from django.core.mail import send_mail
from django.template import loader

from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from .errores import *


AFORO_MAXIMO = settings.AFORO_MAXIMO
MAX_ARAGON =  settings.MAX_ARAGON
MAX_FUERA_ARAGON = settings.MAX_FUERA_ARAGON
# TALLER_MAXIMO = settings.TALLER_MAXIMO


def make_token(email):
    return TimestampSigner().sign(email)

def inscribeme(request):
	email_template_name = 'asistentes/correo_confirmacion.html'
	subject_template_name = _('Confirmación de solicitud de participación')
	
	mensaje = loader.get_template('asistentes/email_confirmacion.txt')

	template_name = 'asistentes/email.html'
	
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = EmailForm(request.POST)

		if form.is_valid():
			# process the data in form.cleaned_data as required
			email = form.cleaned_data.get('email')
			email, token = make_token(email).split(":", 1)
			context = {'token': token, 'email': email}
			send_mail('Solicitud de participación el en I Congreso Internacional de Innovación Educativa',
				mensaje.render(context , request ),
				None,
				(email,),
				)
			return redirect('gracias_solicitud')

    # if a GET (or any other method) we'll create a blank form
	else:
		form = EmailForm()

	return render(request, 'asistentes/email.html', {'form': form})

def error(request):
	error = request.session.pop('error', '')
	contexto = {'error': error}
	return render(request, 'asistentes/errores.html', contexto)
	

def completar(request, *args, **kwargs):
	token = kwargs.get('token', '')
	email = kwargs.get('email', '')
	#print ( '***', kwargs)
	existe = False
	try: 
		Participante.objects.get(email=email)
		existe = True
	except:
		pass
	if existe:
		request.session['error'] = 'Ya se ha inscrito un participante con esta dirección \
		de correo electrónico: {}.'.format(email)
		return redirect('/inscripcion/error')
	try:
		key = '%s:%s' % (email, token)
		TimestampSigner().unsign(key, max_age=1 * 60 * 60)
	except (BadSignature, SignatureExpired):
		request.session['error'] = ERROR_TOKEN
		
		return redirect('/inscripcion/error')
	if Participante.objects.count() >= AFORO_MAXIMO:
		request.session['error'] = 'Se ha completado el aforo del Congreso. Puedes apuntarte a la lista de espera'
		return redirect('/inscripcion/error')

	if request.method == 'POST':
		form = AsistenteForm(request.POST)
		if form.is_valid():
			ca = form.cleaned_data.get('comunidad_autonoma')
			if ca =='Aragón':
				if Participante.objects.filter(Q(comunidad_autonoma='Aragón')).count() >= MAX_ARAGON:
					request.session['error'] = E_MAX_ARAGON
					return redirect('/inscripcion/error')

			else:
				if Participante.objects.filter(~Q(comunidad_autonoma='Aragón')).count() >= MAX_FUERA_ARAGON:
					request.session['error'] = E_MAX_FUERA_ARAGON
					return redirect('/inscripcion/error')

			participante = form.save(commit=False)
			participante.email = email
			participante.save()
			return redirect('gracias', permanent=True )
	else:
		form = AsistenteForm()

	return render(request, 'asistentes/formulario_asistente.html', {'form': form})



def inscribeme_lista_espera(request):
	email_template_name = 'asistentes/correo_confirmacion_espera.html'
	subject_template_name = _('Confirmación de solicitud de participación')
	
	mensaje = loader.get_template('asistentes/email_confirmacion_.txt')

	template_name = 'asistentes/email.html'
	
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = EmailForm(request.POST)

		if form.is_valid():
			# process the data in form.cleaned_data as required
			email = form.cleaned_data.get('email')
			email, token = make_token(email).split(":", 1)
			context = {'token': token, 'email': email}
			send_mail('Solicitud de participación el en I Congreso Internacional de Innovación Educativa',
				mensaje.render(context , request ),
				None,
				(email,),
				)
			return redirect('gracias_solicitud')

    # if a GET (or any other method) we'll create a blank form
	else:
		form = EmailForm()



@login_required
def exportar_inscritos(request):
	''' 
	Test para exportar datos de inscritos
	'''
	f = StringIO()
	writer = csv.writer(f)

	datos = 'nombre apellidos nif activo signos traduccion centro_educativo comunidad_autonoma'.split()
	writer.writerow([smart_str(d) for d in datos])

	for obj in UsuarioTalleres.objects.all():
		writer.writerow([smart_str(getattr(obj, k)) for k in datos])

	response = StreamingHttpResponse(f.getvalue(), content_type="text/csv")
	response['Content-Disposition'] = 'attachment; filename="inscritos_congreso.csv"'    
	return response


def gracias(request, template_name='asistentes/gracias.html'):
	return render(request, template_name)

def gracias_solicitud(request, template_name='asistentes/gracias_solicitud.html'):
	
	return render(request, template_name, {})



### Lista de espera
def inscribeme_lista_espera(request):
	#email_template_name = 'asistentes/correo_confirmacion_espera.html'
	subject_template_name = _('Confirmación de solicitud de participación')
	
	mensaje = loader.get_template('asistentes/email_confirmacion_espera.txt')
	
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = EmailForm(request.POST)

		if form.is_valid():
			# process the data in form.cleaned_data as required
			email = form.cleaned_data.get('email')
			email, token = make_token(email).split(":", 1)
			context = {'token': token, 'email': email}
			send_mail('Solicitud de participación lista de espera en I Congreso Internacional de Innovación Educativa',
				mensaje.render(context , request ),
				None,
				(email,),
				)
			return redirect('gracias_solicitud_espera')

    # if a GET (or any other method) we'll create a blank form
	else:
		form = EmailForm()

	return render(request, 'asistentes/email_espera.html', {'form': form})

def gracias_espera(request, template_name='asistentes/gracias_espera.html'):
	return render(request, template_name)

def gracias_solicitud_espera(request, template_name='asistentes/gracias_solicitud_espera.html'):
	return render(request, template_name, {})


def completar_lista_espera(request, *args, **kwargs):
	token = kwargs.get('token', '')
	email = kwargs.get('email', '')
	existe = False
	try: 
		ListaDeEspera.objects.get(email=email)
		existe = True
	except:
		pass
	if existe:
		request.session['error'] = 'Ya se ha inscrito un participante con esta dirección \
		de correo electrónico: {}.'.format(email)
		return redirect('/inscripcion/error')
	try:
		key = '%s:%s' % (email, token)
		TimestampSigner().unsign(key, max_age=1 * 60 * 60)
	except (BadSignature, SignatureExpired):
		request.session['error'] = ERROR_TOKEN
		return redirect('/inscripcion/error')

	if request.method == 'POST':
		form = EsperaForm(request.POST)
		if form.is_valid():
			participante = form.save(commit=False)
			participante.email = email
			participante.save()
			return redirect('gracias_espera', permanent=True )
	else:
		form = EsperaForm()

	return render(request, 'asistentes/formulario_espera.html', {'form': form})