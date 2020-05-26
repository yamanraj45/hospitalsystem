from django import forms
from .models import detail, appointment


class PatientForm(forms.ModelForm):
   
    class Meta:
        model = detail
        fields =('name','phone_number','location','blood_group','ward_type','doctor')

        def __init__(self,*arg,**kwargs):
            super(detail,self),__init__(*args,**kwargs)
            self.fields['ward_type'].empty_label ="Select Ward Type"


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = appointment
        fields=('date','time','doctor','patient_name')