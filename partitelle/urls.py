from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('registraGiocatore/', views.create, name='registraGiocatore'),
    path('registrazione/', views.registrazione, name='registrazione'),
    path('registrazione/createUser/', views.createUser, name='createUser'),
    path('registraGiocatore/createData/', views.createData, name='createData'),
    path('giocatori/', views.giocatori, name='giocatori'),
    path('giocatori/cancellati/<int:id>', views.delete, name='cancellati'),
    path('giocatori/update/<int:id>', views.update, name='update'),
    path('giocatori/updateData/<int:id>', views.updateData, name='updateData'),
    path('login/', views.login_page, name='login'),
    path('login_req/', views.login_req, name='login_req'),
    path('logout/', views.logout_page, name='logout'),
    path('profilo/', views.profilo, name='profilo'),
    path('statistiche/', views.stat_page, name='statistiche'),
]