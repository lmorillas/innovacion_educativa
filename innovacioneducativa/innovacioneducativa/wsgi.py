"""
WSGI config for innovacioneducativa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

from __future__ import absolute_import, unicode_literals

import os

from django.core.wsgi import get_wsgi_application



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "innovacioneducativa.settings.dev")

application = get_wsgi_application()


'''
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "innovacioneducativa.settings.dev")

_application = get_wsgi_application()


def application(environ, start_response):
    
    if 'PATH_INFO' in environ:
        path_info = environ['PATH_INFO']

    if 'SCRIPT_NAME' in environ:
        script_name = environ['SCRIPT_NAME']

    if 'REQUEST_URI' in environ:
        request_uri = environ['REQUEST_URI']

    output = 'PATH_INFO: ' + repr(path_info) + '\n' + \
             'SCRIPT_NAME: ' + repr(script_name) + '\n' + \
             'REQUEST_URL: ' + repr(request_uri) + '\n'

    print( output )

    #if environ.get('PATH_INFO', '').startswith('/congreso'):
    #	environ['PATH_INFO'] = environ['PATH_INFO'][9:]


    return _application(environ, start_response)

'''