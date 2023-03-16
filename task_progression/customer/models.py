from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_firstname = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15, null=True)
    
    
