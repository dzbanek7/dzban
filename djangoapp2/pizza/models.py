from django.db import models

class Pizza(models.Model):
    LARGE = 'L'
    MEDIUM = 'M'
    SMALL = 'S'
    ROZMIARY = (
        (LARGE, 'duża'),
        (MEDIUM, 'średnia'),
        (SMALL, 'mała'),
    )
    nazwa = models.CharField(verbose_name='pizza', max_length=30, help_text='Nazwa pizzy')
    opis = models.TextField(blank=True, default='', help_text='Opis pizzy')
    rozmiar = models.CharField(max_length=1, choices=ROZMIARY, default=LARGE)
    cena = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    data = models.DateField('dodano', auto_now_add=True)

    def __str__(self):
        return self.nazwa;
    class Meta:
        verbose_name_plural = "pizze"

class Skladnik(models.Model):
    pizze = models.ManyToManyField(Pizza, related_name='skladniki', null=True, blank=True)
    nazwa = models.CharField('składnik', max_length=30)
    jarski = models.BooleanField(
        'jarski?',
        help_text='Zaznacz, jeżeli składnik jest odpowiedni dla wegetarian',
        default=False)
    cena = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    def __str__(self):
        return self.nazwa
    class Meta:
        verbose_name_plural = "skladniki"