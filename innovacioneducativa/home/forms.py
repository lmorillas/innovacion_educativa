from django import forms

from home.models import PreguntaMesa

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab
from crispy_forms.layout import Submit, Button
from crispy_forms.bootstrap import FormActions


class PreguntaMesaForm(forms.ModelForm):
	"""
	Fromulario para preguntas a la mesa redonda
	"""
	helper = FormHelper()
	helper.form_class = 'form-horizontal'
	helper.label_class = 'col-md-4 col-xs-12'
	helper.field_class = 'col-md-8 col-xs-12'
	helper.add_input(Submit('submit', 'Enviar mi pregunta', css_class='btn-primary'))

	class Meta:
		model = PreguntaMesa
		fields = ['pregunta', 'quien']
