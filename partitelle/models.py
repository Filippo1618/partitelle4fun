from django.db import models
from django.contrib.auth.admin import User 
from django.contrib import admin
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.admin import UserAdmin

# Create your models here.

class Giocatore(models.Model):
    nome = models.CharField(max_length=40, default='*')
    descrizione = models.CharField(max_length=450, default='*')
    
    portiere= models.BooleanField(default=False)
    difensore = models.BooleanField(default=False)
    ala_sinistra= models.BooleanField(default=False)
    ala_destra = models.BooleanField(default=False)
    punta = models.BooleanField(default=False)
    