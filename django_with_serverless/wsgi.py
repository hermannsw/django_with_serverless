"""
WSGI config for django_with_serverless project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

try:
  import unzip_requirements
except ImportError:
  pass

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_with_serverless.settings')

application = get_wsgi_application()
