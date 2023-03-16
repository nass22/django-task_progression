import uuid
from django.db import models

# Create your models here.
class Van(models.Model):
    customer_id = models.ForeignKey('customer', on_delete=models.CASCADE)
    tracking_id = models.UUIDField(primary_key=False, default=uuid.uuid4)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    
    work_requested = models.TextField(max_length=None)
    work_progress_percentage = models.IntegerField(min_value=0, max_value=100)
    work_progress_done = models.TextField(max_length=None)
    pictures = models.ImageField(upload_to='images/van/')