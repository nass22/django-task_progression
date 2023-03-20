from django.contrib import admin
from .models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin): #permet de personnaliser l'affichage dans le panel admin
    list_display = ('name', 'firstname', 'email', 'phone')
    
admin.site.register(Customer, CustomerAdmin) # permet d'ajouter Customer dans le panel Admin



