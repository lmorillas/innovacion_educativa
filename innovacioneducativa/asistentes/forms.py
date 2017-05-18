from django import forms
from .models import UsuarioTalleres

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab
from crispy_forms.layout import Submit, Button
from crispy_forms.bootstrap import FormActions

from home.models import Taller
from asistentes.models import UsuarioTalleres, ListaDeEspera
from django.conf import settings

AFORO_MAXIMO = settings.AFORO_MAXIMO
TALLER_MAXIMO = settings.TALLER_MAXIMO

class ListaDeEsperaForm(forms.ModelForm):
	helper = FormHelper()
	helper.form_class = 'form-horizontal'
	helper.label_class = 'col-md-2 col-xs-12'
	helper.field_class = 'col-md-6 col-xs-12'
	helper.add_input(Submit('submit', 'Añadir a lista de espera'))

	class Meta:
	    model = ListaDeEspera
	    
	    exclude=['user']


class TalleresForm(forms.ModelForm):
	helper = FormHelper()
	helper.form_class = 'form-horizontal'
	helper.label_class = 'col-md-2 col-xs-12'
	helper.field_class = 'col-md-6 col-xs-12'
	helper.add_input(Submit('submit', 'Realizar inscripción', css_class='btn-primary'))
	#helper.add_input(Button('cancel', 'Cancelar'))


	class Meta:
	    model = UsuarioTalleres
	    exclude=['user']

	def clean(self):
		cleaned_data = super(TalleresForm, self).clean()
		   
		if UsuarioTalleres.objects.count() >= AFORO_MAXIMO: 
			raise forms.ValidationError(
	                    "Se ha completado el aforo, puedes apuntarte en la liststa de espera."
	                )
		t1 = cleaned_data.get('taller1')
		t2 = cleaned_data.get('taller2')
		t3 = cleaned_data.get('taller3')
		t4 = cleaned_data.get('taller4')
		talleres = [t for t in [t1, t2, t3, t4] if t]
		if len(talleres) != len(set(talleres)):
			raise forms.ValidationError(
	                    "Has elegido dos veces el mismo taller."
	                )
		return cleaned_data

	def completo_taller(self, n, valor):
		return getattr(Taller.objects.get(nombre=valor), n).count() >= TALLER_MAXIMO

	def clean_taller1(self):
		data = self.cleaned_data['taller1']
		if data and 'taller1' in self.changed_data and self.completo_taller('taller1', data):
				raise forms.ValidationError("Este taller está completo")
		return data

	def clean_taller2(self):
		data = self.cleaned_data['taller2']
		if data and 'taller2' in self.changed_data and self.completo_taller('taller2', data):
				raise forms.ValidationError("Este taller está completo")
		return data

	def clean_taller3(self):
		data = self.cleaned_data['taller3']
		if data and 'taller3' in self.changed_data and self.completo_taller('taller3', data):
			raise forms.ValidationError("Este taller está completo")
		return data

	def clean_taller4(self):
		data = self.cleaned_data['taller4']
		if data and 'taller4' in self.changed_data and self.completo_taller('taller4', data):
			raise forms.ValidationError("Este taller está completo")
		return data


	#def clean_user(self):
	#	return request.user

'''

helper.form_class = 'form-horizontal'
helper.label_class = 'col-lg-2'
helper.field_class = 'col-lg-8'
helper.layout = Layout(
    'email',
    'password',
    'remember_me',
    StrictButton('Sign in', css_class='btn-default'),
)
'''

'''

	#helper.form_tag = False
	helper.layout = Layout(
	    TabHolder(
            Tab(
            	'Datos personales',
                'nombre',
                'apellidos',
                'nif'
            ),
            Tab(
            	'Centro de trabajo',
                'activo',
                'centro_educativo',
                'comunidad_autonoma',
                
            ),
            Tab(
            	'Selección de talleres',
                'taller1',
                'taller2',
                'taller3',
                'taller4',
                
            )
        )
    )
    '''