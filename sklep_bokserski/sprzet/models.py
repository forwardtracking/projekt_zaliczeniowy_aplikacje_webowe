from decimal import Decimal

from django.db import models


POZIOM_CHOICES = [
    ("poczatkujacy", "Początkujący"),
    ("sredniozaawansowany", "Średniozaawansowany"),
    ("zaawansowany", "Zaawansowany"),
]

ZAPIECIE_CHOICES = [
    ("rzep", "Rzep"),
    ("sznurowane", "Sznurowane"),
]

DOPASOWANIE_CHOICES = [
    ("boil_bite", "Boil & Bite"),
    ("custom", "Custom"),
    ("pasek", "Z paskiem"),
]

ROZMIAR_CHOICES = [
    ("S", "S"),
    ("M", "M"),
    ("L", "L"),
    ("XL", "XL"),
]


class Rekawice(models.Model):
    nazwa = models.CharField(max_length=120, verbose_name="Nazwa")
    marka = models.CharField(max_length=80, verbose_name="Marka")
    waga_oz = models.PositiveIntegerField(verbose_name="Waga (oz)")
    material = models.CharField(max_length=80, verbose_name="Materiał")
    zapiecie = models.CharField(
        max_length=12,
        choices=ZAPIECIE_CHOICES,
        default="rzep",
        verbose_name="Zapięcie",
    )
    poziom = models.CharField(
        max_length=20, choices=POZIOM_CHOICES, verbose_name="Poziom"
    )
    cena = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Cena (PLN)")
    opis = models.TextField(blank=True, verbose_name="Opis")
    utworzono = models.DateTimeField(auto_now_add=True, verbose_name="Dodano")

    class Meta:
        verbose_name = "Rękawice bokserskie"
        verbose_name_plural = "Rękawice bokserskie"
        ordering = ["nazwa"]

    def __str__(self):
        return f"{self.marka} {self.nazwa}"


class Buty(models.Model):
    nazwa = models.CharField(max_length=120, verbose_name="Nazwa")
    marka = models.CharField(max_length=80, verbose_name="Marka")
    rozmiar_eu = models.DecimalField(
        max_digits=4, decimal_places=1, verbose_name="Rozmiar EU"
    )
    wsparcie_kostki = models.BooleanField(default=True, verbose_name="Wsparcie kostki")
    material = models.CharField(max_length=80, verbose_name="Materiał")
    poziom = models.CharField(
        max_length=20, choices=POZIOM_CHOICES, verbose_name="Poziom"
    )
    cena = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Cena (PLN)")
    opis = models.TextField(blank=True, verbose_name="Opis")
    utworzono = models.DateTimeField(auto_now_add=True, verbose_name="Dodano")

    class Meta:
        verbose_name = "Buty do boksu"
        verbose_name_plural = "Buty do boksu"
        ordering = ["nazwa"]

    def __str__(self):
        return f"{self.marka} {self.nazwa}"


class Ochraniacze(models.Model):
    nazwa = models.CharField(max_length=120, verbose_name="Nazwa")
    marka = models.CharField(max_length=80, verbose_name="Marka")
    dopasowanie = models.CharField(
        max_length=20, choices=DOPASOWANIE_CHOICES, verbose_name="Dopasowanie"
    )
    rozmiar = models.CharField(
        max_length=4, choices=ROZMIAR_CHOICES, verbose_name="Rozmiar"
    )
    cena = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Cena (PLN)")
    opis = models.TextField(blank=True, verbose_name="Opis")
    utworzono = models.DateTimeField(auto_now_add=True, verbose_name="Dodano")

    class Meta:
        verbose_name = "Ochraniacz na zęby"
        verbose_name_plural = "Ochraniacze na zęby"
        ordering = ["nazwa"]

    def __str__(self):
        return f"{self.marka} {self.nazwa}"


class Owijki(models.Model):
    nazwa = models.CharField(max_length=120, verbose_name="Nazwa")
    marka = models.CharField(max_length=80, verbose_name="Marka")
    dlugosc_cm = models.PositiveIntegerField(verbose_name="Długość (cm)")
    elastyczne = models.BooleanField(default=True, verbose_name="Elastyczne")
    material = models.CharField(max_length=80, verbose_name="Materiał")
    cena = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Cena (PLN)")
    opis = models.TextField(blank=True, verbose_name="Opis")
    utworzono = models.DateTimeField(auto_now_add=True, verbose_name="Dodano")

    class Meta:
        verbose_name = "Owijki"
        verbose_name_plural = "Owijki"
        ordering = ["nazwa"]

    def __str__(self):
        return f"{self.marka} {self.nazwa}"


class Zestawy(models.Model):
    nazwa = models.CharField(max_length=120, verbose_name="Nazwa zestawu")
    poziom = models.CharField(
        max_length=20, choices=POZIOM_CHOICES, verbose_name="Poziom"
    )
    rekawice = models.ForeignKey(
        Rekawice,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sparring_sets",
        verbose_name="Rękawice",
    )
    buty = models.ForeignKey(
        Buty,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sparring_sets",
        verbose_name="Buty",
    )
    ochraniacz = models.ForeignKey(
        Ochraniacze,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sparring_sets",
        verbose_name="Ochraniacz na zęby",
    )
    owijki = models.ForeignKey(
        Owijki,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sparring_sets",
        verbose_name="Owijki",
    )
    cena_zestawu = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Cena zestawu (PLN)"
    )
    uwagi = models.TextField(blank=True, verbose_name="Uwagi")
    utworzono = models.DateTimeField(auto_now_add=True, verbose_name="Dodano")

    class Meta:
        verbose_name = "Sparring set"
        verbose_name_plural = "Sparring sety"
        ordering = ["-utworzono"]

    def __str__(self):
        return f"{self.nazwa} ({self.get_poziom_display()})"

    @property
    def suma_cen_regularnych(self):
        total = Decimal("0.00")
        for item in [self.rekawice, self.buty, self.ochraniacz, self.owijki]:
            if item:
                total += item.cena
        return total
