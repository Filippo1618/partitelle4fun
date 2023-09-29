from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Giocatore
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from . decorators import login_required_for_registration

# Create your views here.

def index(request):
    template = loader.get_template('partitelle/index.html')
    return HttpResponse(template.render({}, request))

def create(request):
    template = loader.get_template('partitelle/registraGiocatore.html')
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


# una wrapped view per impedire a chi ha fatto il log in di registrarsi senza prima fare logout
def login_required_for_registration(view_func):
    def _wrapped_view(request, *args, **kwargs):
        # Verifica se l'utente è autenticato
        if request.user.is_authenticated:
            messages.error(request,"Devi fare il log out prima di procedere con la registrazione di un account")
            # Utente già autenticato, reindirizza a una pagina specifica (ad esempio il profilo)
            return redirect('profilo')  # Cambia questo percorso in base alla tua configurazione
        else:
            # Utente non autenticato, permetti l'accesso alla pagina di registrazione
            return view_func(request, *args, **kwargs)
    return _wrapped_view


def createUser(request):
    
    template = loader.get_template('partitelle/login.html')

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        nome = request.POST['nome']
        cognome = request.POST['cognome']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username):
            messages.error(request, 'Username already exists')
            return HttpResponseRedirect(reverse('registrazione'))
        
        if User.objects.filter(email=email):
            messages.error(request, 'Username already exists')
            return HttpResponseRedirect(reverse('registrazione'))

        if len(username) > 10:
            messages.error(request, "Username too long")
            return HttpResponseRedirect(reverse('registrazione'))
        
        if password1 != password2:
            messages.error(request, "Le password non coincidono")
            return HttpResponseRedirect(reverse('registrazione'))
        
        if not username.isalnum():
            messages.error(request, "l' username deve essere alfanumerico")
            return HttpResponseRedirect(reverse('registrazione'))
                                        
        new_user = User.objects.create_user(username=username, password=password1)
        new_user.first_name = nome
        new_user.email = email
        new_user.last_name = cognome

        new_user.save()

        messages.success(request,"Il tuo account è stato creato correttamente!")
        return HttpResponseRedirect(reverse('login'))
    return HttpResponse( template.render({}, request))


@login_required_for_registration
def registrazione(request):
    
    template = loader.get_template('partitelle/registrazione.html')
    return HttpResponse( template.render({},request))


def login_page(request):
    
    template = loader.get_template('partitelle/login.html')
    return HttpResponse( template.render({},request))


def login_req(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            template = loader.get_template('partitelle/login.html') #da sostituire con profilo
            context = {
                "user": user
            }
            return HttpResponse(template.render(context,request))
        else:
            messages.error(request,"username o passsword errati")
            return HttpResponseRedirect(reverse('login'))
    
    return HttpResponseRedirect(reverse('login'))


def logout_page(request):
    logout(request)
    messages.error(request,"logout effettuato correttamente")
    return HttpResponseRedirect(reverse('login'))

@login_required
def profilo(request):

    template = loader.get_template('partitelle/profilo.html')

    # Ottieni l'oggetto UserProfile associato all'utente
    user = request.user
    template = loader.get_template('partitelle/profilo.html')

    context = {
        'user': user,  # Passa l'oggetto User al template
    }

    return HttpResponse( template.render(context ,request))


@login_required
def stat_page(request):

    user = request.user

    template = loader.get_template('partitelle/statistiche.html')

    context = {
        "user": user,
    }

    return HttpResponse(template.render(context, request))
