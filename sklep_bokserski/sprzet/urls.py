from django.urls import path

from . import views

app_name = "sprzet"

urlpatterns = [
    path("", views.RekawiceListView.as_view(), name="home"),
    # Rękawice
    path("rekawice/", views.RekawiceListView.as_view(), name="rekawice_lista"),
    path("rekawice/dodaj/", views.RekawiceCreateView.as_view(), name="rekawice_dodaj"),
    path(
        "rekawice/<int:pk>/",
        views.RekawiceDetailView.as_view(),
        name="rekawice_szczegoly",
    ),
    path(
        "rekawice/<int:pk>/edytuj/",
        views.RekawiceUpdateView.as_view(),
        name="rekawice_edytuj",
    ),
    path(
        "rekawice/<int:pk>/usun/",
        views.RekawiceDeleteView.as_view(),
        name="rekawice_usun",
    ),
    # Buty
    path("buty/", views.ButyListView.as_view(), name="buty_lista"),
    path("buty/dodaj/", views.ButyCreateView.as_view(), name="buty_dodaj"),
    path("buty/<int:pk>/", views.ButyDetailView.as_view(), name="buty_szczegoly"),
    path("buty/<int:pk>/edytuj/", views.ButyUpdateView.as_view(), name="buty_edytuj"),
    path("buty/<int:pk>/usun/", views.ButyDeleteView.as_view(), name="buty_usun"),
    # Ochraniacze
    path(
        "ochraniacze/",
        views.OchraniaczeListView.as_view(),
        name="ochraniacze_lista",
    ),
    path(
        "ochraniacze/dodaj/",
        views.OchraniaczeCreateView.as_view(),
        name="ochraniacze_dodaj",
    ),
    path(
        "ochraniacze/<int:pk>/",
        views.OchraniaczeDetailView.as_view(),
        name="ochraniacze_szczegoly",
    ),
    path(
        "ochraniacze/<int:pk>/edytuj/",
        views.OchraniaczeUpdateView.as_view(),
        name="ochraniacze_edytuj",
    ),
    path(
        "ochraniacze/<int:pk>/usun/",
        views.OchraniaczeDeleteView.as_view(),
        name="ochraniacze_usun",
    ),
    # Owijki
    path("owijki/", views.OwijkiListView.as_view(), name="owijki_lista"),
    path("owijki/dodaj/", views.OwijkiCreateView.as_view(), name="owijki_dodaj"),
    path("owijki/<int:pk>/", views.OwijkiDetailView.as_view(), name="owijki_szczegoly"),
    path("owijki/<int:pk>/edytuj/", views.OwijkiUpdateView.as_view(), name="owijki_edytuj"),
    path("owijki/<int:pk>/usun/", views.OwijkiDeleteView.as_view(), name="owijki_usun"),
    # Zestawy
    path("zestawy/", views.ZestawyListView.as_view(), name="zestawy_lista"),
    path("zestawy/dodaj/", views.ZestawyCreateView.as_view(), name="zestawy_dodaj"),
    path(
        "zestawy/<int:pk>/",
        views.ZestawyDetailView.as_view(),
        name="zestawy_szczegoly",
    ),
    path(
        "zestawy/<int:pk>/edytuj/",
        views.ZestawyUpdateView.as_view(),
        name="zestawy_edytuj",
    ),
    path("zestawy/<int:pk>/usun/", views.ZestawyDeleteView.as_view(), name="zestawy_usun"),
    # Dodatkowe widoki
    path("marki/", views.szukaj_marki, name="marka_szukaj"),
    path("marki/<str:marka>/", views.katalog_marki, name="marka_katalog"),
    path("statystyki/", views.statystyki_sprzetu, name="statystyki"),
]
