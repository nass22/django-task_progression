import uuid
from django.db import models
from customer.models import Customer

# Create your models here.
class Van(models.Model):
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    work_requested = models.TextField(max_length=None)
    
    def __str__(self):
        name = str(self.customer)
        return name

class Work_tracking(models.Model):
    van = models.ForeignKey(Van, on_delete=models.CASCADE)
    tracking_id = models.UUIDField(primary_key=False, default=uuid.uuid4)
    work_progress_percentage = models.IntegerField()
    work_progress_done = models.TextField(max_length=None)
    finish = models.BooleanField(default=False)
    
    def __str__(self):
        name = str(self.van)
        return name
    
class Img_tracking(models.Model):
    van = models.ForeignKey(Van, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/van/')
    
    def __str__(self):
        name = str(self.van)
        return name
    

    
