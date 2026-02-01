from django.db.models import Avg, Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Buty, Ochraniacze, Owijki, Rekawice, Zestawy


class SprzetFormContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_verbose_name"] = self.model._meta.verbose_name
        return context


class RekawiceListView(ListView):
    model = Rekawice
    template_name = "sprzet/rekawice_list.html"
    context_object_name = "items"


class RekawiceDetailView(DetailView):
    model = Rekawice
    template_name = "sprzet/rekawice_detail.html"


class RekawiceCreateView(SprzetFormContextMixin, CreateView):
    model = Rekawice
    fields = [
        "nazwa",
        "marka",
        "waga_oz",
        "material",
        "zapiecie",
        "poziom",
        "cena",
        "opis",
    ]
    template_name = "sprzet/formularz.html"
    success_url = reverse_lazy("sprzet:rekawice_lista")


class RekawiceUpdateView(SprzetFormContextMixin, UpdateView):
    model = Rekawice
    fields = [
        "nazwa",
        "marka",
        "waga_oz",
        "material",
        "zapiecie",
        "poziom",
        "cena",
        "opis",
    ]
    template_name = "sprzet/formularz.html"
    success_url = reverse_lazy("sprzet:rekawice_lista")


class RekawiceDeleteView(DeleteView):
    model = Rekawice
    template_name = "sprzet/potwierdz_usun.html"
    success_url = reverse_lazy("sprzet:rekawice_lista")


class ButyListView(ListView):
    model = Buty
    template_name = "sprzet/buty_list.html"
    context_object_name = "items"


class ButyDetailView(DetailView):
    model = Buty
    template_name = "sprzet/buty_detail.html"


class ButyCreateView(SprzetFormContextMixin, CreateView):
    model = Buty
    fields = [
        "nazwa",
        "marka",
        "rozmiar_eu",
        "wsparcie_kostki",
        "material",
        "poziom",
        "cena",
        "opis",
    ]
    template_name = "sprzet/formularz.html"
    success_url = reverse_lazy("sprzet:buty_lista")


class ButyUpdateView(SprzetFormContextMixin, UpdateView):
    model = Buty
    fields = [
        "nazwa",
        "marka",
        "rozmiar_eu",
        "wsparcie_kostki",
        "material",
        "poziom",
        "cena",
        "opis",
    ]
    template_name = "sprzet/formularz.html"
    success_url = reverse_lazy("sprzet:buty_lista")


class ButyDeleteView(DeleteView):
    model = Buty
    template_name = "sprzet/potwierdz_usun.html"
    success_url = reverse_lazy("sprzet:buty_lista")


class OchraniaczeListView(ListView):
    model = Ochraniacze
    template_name = "sprzet/ochraniacze_list.html"
    context_object_name = "items"


class OchraniaczeDetailView(DetailView):
    model = Ochraniacze
    template_name = "sprzet/ochraniacze_detail.html"


class OchraniaczeCreateView(SprzetFormContextMixin, CreateView):
    model = Ochraniacze
    fields = [
        "nazwa",
        "marka",
        "dopasowanie",
        "rozmiar",
        "cena",
        "opis",
    ]
    template_name = "sprzet/formularz.html"
    success_url = reverse_lazy("sprzet:ochraniacze_lista")


class OchraniaczeUpdateView(SprzetFormContextMixin, UpdateView):
    model = Ochraniacze
    fields = [
        "nazwa",
        "marka",
        "dopasowanie",
        "rozmiar",
        "cena",
        "opis",
    ]
    template_name = "sprzet/formularz.html"
    success_url = reverse_lazy("sprzet:ochraniacze_lista")


class OchraniaczeDeleteView(DeleteView):
    model = Ochraniacze
    template_name = "sprzet/potwierdz_usun.html"
    success_url = reverse_lazy("sprzet:ochraniacze_lista")


class OwijkiListView(ListView):
    model = Owijki
    template_name = "sprzet/owijki_list.html"
    context_object_name = "items"


class OwijkiDetailView(DetailView):
    model = Owijki
    template_name = "sprzet/owijki_detail.html"


class OwijkiCreateView(SprzetFormContextMixin, CreateView):
    model = Owijki
    fields = [
        "nazwa",
        "marka",
        "dlugosc_cm",
        "elastyczne",
        "material",
        "cena",
        "opis",
    ]
    template_name = "sprzet/formularz.html"
    success_url = reverse_lazy("sprzet:owijki_lista")


class OwijkiUpdateView(SprzetFormContextMixin, UpdateView):
    model = Owijki
    fields = [
        "nazwa",
        "marka",
        "dlugosc_cm",
        "elastyczne",
        "material",
        "cena",
        "opis",
    ]
    template_name = "sprzet/formularz.html"
    success_url = reverse_lazy("sprzet:owijki_lista")


class OwijkiDeleteView(DeleteView):
    model = Owijki
    template_name = "sprzet/potwierdz_usun.html"
    success_url = reverse_lazy("sprzet:owijki_lista")


class ZestawyListView(ListView):
    model = Zestawy
    template_name = "sprzet/zestawy_list.html"
    context_object_name = "items"


class ZestawyDetailView(DetailView):
    model = Zestawy
    template_name = "sprzet/zestawy_detail.html"


class ZestawyCreateView(SprzetFormContextMixin, CreateView):
    model = Zestawy
    fields = [
        "nazwa",
        "poziom",
        "rekawice",
        "buty",
        "ochraniacz",
        "owijki",
        "cena_zestawu",
        "uwagi",
    ]
    template_name = "sprzet/formularz.html"
    success_url = reverse_lazy("sprzet:zestawy_lista")


class ZestawyUpdateView(SprzetFormContextMixin, UpdateView):
    model = Zestawy
    fields = [
        "nazwa",
        "poziom",
        "rekawice",
        "buty",
        "ochraniacz",
        "owijki",
        "cena_zestawu",
        "uwagi",
    ]
    template_name = "sprzet/formularz.html"
    success_url = reverse_lazy("sprzet:zestawy_lista")


class ZestawyDeleteView(DeleteView):
    model = Zestawy
    template_name = "sprzet/potwierdz_usun.html"
    success_url = reverse_lazy("sprzet:zestawy_lista")


def katalog_marki(request, marka):
    context = {
        "marka": marka,
        "rekawice": Rekawice.objects.filter(marka__iexact=marka),
        "buty": Buty.objects.filter(marka__iexact=marka),
        "ochraniacze": Ochraniacze.objects.filter(marka__iexact=marka),
        "owijki": Owijki.objects.filter(marka__iexact=marka),
        "zestawy": Zestawy.objects.filter(nazwa__icontains=marka),
    }
    return render(request, "sprzet/marka_katalog.html", context)


def szukaj_marki(request):
    marka = (request.GET.get("q") or "").strip()
    context = {
        "marka": marka,
        "rekawice": Rekawice.objects.filter(marka__iexact=marka) if marka else [],
        "buty": Buty.objects.filter(marka__iexact=marka) if marka else [],
        "ochraniacze": Ochraniacze.objects.filter(marka__iexact=marka)
        if marka
        else [],
        "owijki": Owijki.objects.filter(marka__iexact=marka) if marka else [],
        "zestawy": Zestawy.objects.filter(nazwa__icontains=marka) if marka else [],
    }
    return render(request, "sprzet/marka_katalog.html", context)


def statystyki_sprzetu(request):
    context = {
        "rekawice": Rekawice.objects.aggregate(count=Count("id"), avg=Avg("cena")),
        "buty": Buty.objects.aggregate(count=Count("id"), avg=Avg("cena")),
        "ochraniacze": Ochraniacze.objects.aggregate(count=Count("id"), avg=Avg("cena")),
        "owijki": Owijki.objects.aggregate(count=Count("id"), avg=Avg("cena")),
        "zestawy": Zestawy.objects.aggregate(
            count=Count("id"), avg=Avg("cena_zestawu")
        ),
    }
    return render(request, "sprzet/statystyki_sprzetu.html", context)
