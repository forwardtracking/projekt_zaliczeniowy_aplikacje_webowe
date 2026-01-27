"""
URL configuration for sprzet_bokserski_sklep project.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("sprzet.urls")),
    path("admin/", admin.site.urls),
]
