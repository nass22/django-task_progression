import uuid
from django.db import models
from customer.models import Customer
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Van(models.Model):
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    work_requested = models.TextField(max_length=None)
    work_progress_percentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    tracking_id = models.UUIDField(primary_key=False, default=uuid.uuid4)
    finish = models.BooleanField(default=False)
    
    def __str__(self):
        name = str(self.customer)
        return name

class Work_tracking(models.Model):
    van = models.ForeignKey(Van, on_delete=models.CASCADE)
    work_progress_done = models.TextField(max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        name = str(self.van)
        return name
    
class Img_tracking(models.Model):
    van = models.ForeignKey(Van, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/van/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        name = str(self.van)
        return name
    

    
