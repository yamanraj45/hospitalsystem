from django.db import models
from doctor.models import DoctorDetail

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
    doctor = models.ForeignKey(DoctorDetail,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name


class appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey(DoctorDetail,on_delete=models.CASCADE)
    patient_name = models.ForeignKey(
        detail,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return "%s Appointment With %s on %s in %s " % (self.patient_name, self.doctor, self.date, self.time)
    