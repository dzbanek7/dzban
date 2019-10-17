from django.db import models


class Miasto(models.Model):
    nazwa = models.CharField(
        verbose_name='miasto',
        max_length=30,
        help_text='Nazwa miasta')
    kod = models.CharField(
        max_length=6,
        help_text='Kod pocztowy')

    def __str__(self):
        return self.nazwa;

    class Meta:
        verbose_name_plural = "Miasta"

class Uczelnia(models.Model):
    nazwa = models.CharField(
        verbose_name='uczelnia',
        max_length=30,
        help_text='Nazwa uczelni')

    def __str__(self):
        return self.nazwa;

    class Meta:
        verbose_name_plural = "Uczelnie"

class Student(models.Model):
    imie = models.CharField('imię', max_length=30)
    nazwisko = models.CharField(max_length=30)
    uczelnia = models.ForeignKey(Uczelnia, on_delete=models.SET_NULL, null=True)
    miasto = models.ForeignKey(Miasto, on_delete=models.SET_NULL, null=True)
    roks = models.CharField('rok studiów', max_length=3)
    dochod = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.imie + " " + self.nazwisko;

    class Meta:
        verbose_name_plural = "Studenci"