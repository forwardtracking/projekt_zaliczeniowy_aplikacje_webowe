"""
ASGI config for sprzet_bokserski_sklep project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sprzet_bokserski_sklep.settings")

application = get_asgi_application()
