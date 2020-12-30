"""
WSGI config for societyaabb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'societyaabb.settings')

application = get_wsgi_application()

"""
import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'societyaabb.settings')

application = Cling(MediaCling(get_wsgi_application()))
"""

