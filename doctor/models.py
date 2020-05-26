from django.db import models

class DoctorDetail(models.Model):
    name = models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    phone_number=models.IntegerField()
    
    def __str__(self):
        return self.name