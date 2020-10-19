from django.db import models

# Create your models here.
class Reports(models.Model):
    name        = models.CharField(max_length=30)
    mobile      = models.CharField(max_length=12)
    email       = models.EmailField(max_length=15)
    dob         = models.DateField()
    gender      = models.CharField(max_length=10)
    age         = models.CharField(max_length=100)
    crimetype   = models.CharField(max_length=100)
    describecrime   =models.TextField(max_length=100)
    crimelocation   =models.CharField(max_length=50)
    youraddress     =models.TextField(max_length=100)
    
    def __str__(self):
        return self.name
    class meta:
        db_table = 'registered_reports'
    






