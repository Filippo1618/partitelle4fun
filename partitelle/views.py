from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Giocatore
# Create your views here.

def index(request):
    template = loader.get_template('partitelle/index.html')
    return HttpResponse(template.render({}, request))

def create(request):
    template = loader.get_template('partitelle/createPage.html')
    return HttpResponse(template.render({}, request))

def createData(request):
    nome = request.POST['nome']
    descrizione = request.POST['descrizione']


    #gli input dei checkbox sono stringhe 'on' / 'off' quindi vanno convertiti in True / False
    portiere = request.POST.get('portiere', False) == 'on'
    difensore = request.POST.get('difensore', False) == 'on'
    ala_sinistra = request.POST.get('ala_sinistra', False) == 'on'
    ala_destra = request.POST.get('ala_destra', False) == 'on'
    punta = request.POST.get('punta', False) == 'on'

    nuovoGiocatore = Giocatore(nome=nome, descrizione=descrizione, portiere=portiere, difensore=difensore, ala_sinistra=ala_sinistra, ala_destra=ala_destra, punta=punta)
    nuovoGiocatore.save()

    return HttpResponseRedirect(reverse("index"))

def delete(request, id):
    giocatoreDaCancellare = Giocatore.objects.get(id=id)
    giocatoreDaCancellare.delete()
    return HttpResponseRedirect(reverse("index"))

def update(request, id):
    template = loader.get_template('partitelle/updatePage.html')
    giocatore_da_aggiornare = Giocatore.objects.get(id=id)

    context = {
        "giocatore": giocatore_da_aggiornare
    }
    print (context["giocatore"].descrizione)
    return HttpResponse(template.render(context, request))

def updateData(request, id):
    nome = request.POST['nome']
    descrizione = request.POST['descrizione']

    giocatore_da_aggiornare = Giocatore.objects.get(id=id)
    giocatore_da_aggiornare.nome = nome
    giocatore_da_aggiornare.descrizione = descrizione
    #gli input dei checkbox sono stringhe 'on' / 'off' quindi vanno convertiti in True / False
    giocatore_da_aggiornare.portiere = request.POST.get('portiere', False) == 'on'
    giocatore_da_aggiornare.difensore = request.POST.get('difensore', False) == 'on'
    giocatore_da_aggiornare.ala_sinistra = request.POST.get('ala_sinistra', False) == 'on'
    giocatore_da_aggiornare.ala_destra = request.POST.get('ala_destra', False) == 'on'
    giocatore_da_aggiornare.punta = request.POST.get('punta', False) == 'on'

    giocatore_da_aggiornare.save()

    return HttpResponseRedirect(reverse("index"))



def giocatori(request):
    giocatori = Giocatore.objects.all().values()
    
    context = {
        "giocatori": giocatori 
    }

    template = loader.get_template('partitelle/campioni.html')
    return HttpResponse(template.render(context, request))