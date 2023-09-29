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

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    eta = models.IntegerField(null= True, blank=True)
    nickname = models.CharField(max_length=50, null=True, blank=True)
    descrizione = models.CharField(max_length=450, default='*')
    
    portiere= models.BooleanField(default=False)
    difensore = models.BooleanField(default=False)
    ala_sinistra= models.BooleanField(default=False)
    ala_destra = models.BooleanField(default=False)
    punta = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname or "nessun nickname fornito"

@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# Define an inline for UserProfile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

# Extend the UserAdmin class
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )  # Add UserProfileInline to the inlines list

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
