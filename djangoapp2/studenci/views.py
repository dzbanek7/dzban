from django.shortcuts import render
from django.http import HttpResponse
from studenci.models import Miasto
from studenci.models import Uczelnia


def index(request):
    return HttpResponse("Witaj w aplikacji Studenci!")
    # return render(request, 'pizza/index.html')


def news(request):
    return HttpResponse("<h1>Nowości u studentów</h1>")
    # return render(request, 'pizza/news.html')

def miasta(request):

    if request.method == 'POST':
        nazwa = request.POST.get('nazwa')
        kod= request.POST.get('kod')
        m = Miasto(nazwa=nazwa, kod=kod)
        m.save()
        print(nazwa)
        print(kod)

    miasta = Miasto.objects.all()
    kontekst = {
        'miasta': miasta
    }
    return render(request, 'studenci/miasta.html', kontekst)

def uczelnie(request):

    if request.method == 'POST':
        nazwa = request.POST.get('nazwa')
        u = Uczelnia(nazwa=nazwa)
        u.save()
        print(nazwa)

    uczelnie = Uczelnia.objects.all()
    kontekst = {
        'uczelnie': uczelnie
    }
    return render(request, 'studenci/uczelnie.html', kontekst)