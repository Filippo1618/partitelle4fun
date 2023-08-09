from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('registrati/', views.create, name='registrazione'),
    path('registrati/createData/', views.createData, name='createData'),
    path('giocatori/', views.giocatori, name='giocatori'),
    path('giocatori/cancellati/<int:id>', views.delete, name='cancellati'),
    path('giocatori/update/<int:id>', views.update, name='update'),
    path('giocatori/updateData/<int:id>', views.updateData, name='updateData'),

]