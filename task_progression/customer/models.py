from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True)
    
    def __str__(self):
        return self.firstname + ' ' + self.name
    
    
