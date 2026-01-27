"""
WSGI config for sprzet_bokserski_sklep project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sprzet_bokserski_sklep.settings")

application = get_wsgi_application()
