from django.db import models

# Create your models here.

class Giocatore(models.Model):
    nome = models.CharField(max_length=40, default='*')
    descrizione = models.CharField(max_length=450, default='*')
    portiere= models.BooleanField(default=False)
    difensore = models.BooleanField(default=False)
    ala_sinistra= models.BooleanField(default=False)
    ala_destra = models.BooleanField(default=False)
    punta = models.BooleanField(default=False)

