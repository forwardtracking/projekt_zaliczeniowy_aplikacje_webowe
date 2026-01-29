from django.contrib import admin

from .models import Buty, Ochraniacze, Owijki, Rekawice, Zestawy


@admin.register(Rekawice)
class RekawiceAdmin(admin.ModelAdmin):
    list_display = ["nazwa", "marka", "waga_oz", "poziom", "cena"]
    list_filter = ["marka", "poziom", "zapiecie"]
    search_fields = ["nazwa", "marka"]


@admin.register(Buty)
class ButyAdmin(admin.ModelAdmin):
    list_display = ["nazwa", "marka", "rozmiar_eu", "wsparcie_kostki", "poziom", "cena"]
    list_filter = ["marka", "poziom", "wsparcie_kostki"]
    search_fields = ["nazwa", "marka"]


@admin.register(Ochraniacze)
class OchraniaczeAdmin(admin.ModelAdmin):
    list_display = ["nazwa", "marka", "dopasowanie", "rozmiar", "cena"]
    list_filter = ["marka", "dopasowanie", "rozmiar"]
    search_fields = ["nazwa", "marka"]


@admin.register(Owijki)
class OwijkiAdmin(admin.ModelAdmin):
    list_display = ["nazwa", "marka", "dlugosc_cm", "elastyczne", "cena"]
    list_filter = ["marka", "elastyczne"]
    search_fields = ["nazwa", "marka"]


@admin.register(Zestawy)
class ZestawyAdmin(admin.ModelAdmin):
    list_display = ["nazwa", "poziom", "cena_zestawu", "utworzono"]
    list_filter = ["poziom"]
    search_fields = ["nazwa"]
