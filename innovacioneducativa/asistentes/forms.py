from django import forms
from .models import UsuarioTalleres

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab
from crispy_forms.layout import Submit

from home.models import Taller

class TalleresForm(forms.ModelForm):
	helper = FormHelper()
	helper.form_class = 'form-horizontal'
	helper.label_class = 'col-md-2 col-xs-12'
	helper.field_class = 'col-md-6 col-xs-12'
	helper.add_input(Submit('submit', 'Realizar inscripción'))


	class Meta:
	    model = UsuarioTalleres
	    widgets = {'user': forms.HiddenInput(),
	    #'taller1': forms.ModelChoiceField(queryset=Taller.objects.all())
	    }
	    exclude = []
	    


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