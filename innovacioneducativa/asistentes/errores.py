E_MAX_ARAGON = 'Se ha superado el número de participantes de la Comunidad Autónoma de Aragón'
E_MAX_FUERA_ARAGON = 'Se ha superado el número de participantes de fuera de la Comunidad Autónoma de Aragón'
ERROR_TOKEN = '''La clave de validación de este correo ha expirado o es incorrecta. 
		Pide una nueva clave en {{ request.scheme }}://{{ request.get_host }}{% url 'email_inscripcion' %}'''