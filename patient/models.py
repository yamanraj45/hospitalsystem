from django.db import models

class ward(models.Model):
    ward_room = models.CharField(max_length=30)
    def __str__(self):
        return self.ward_room



class detail(models.Model):
    name = models.CharField(max_length = 100)
    phone_number = models.IntegerField()
    blood_group = models.CharField(max_length=3)
    location = models.CharField(max_length=100)
    ward_type = models.ForeignKey(ward,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

