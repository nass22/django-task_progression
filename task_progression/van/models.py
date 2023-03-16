from django.db import models

# Create your models here.
class Van(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    customer_firstname = models.CharField(max_length=200)
    work_requested = models.
