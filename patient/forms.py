from django import forms
from .models import detail, appointment


class PatientForm(forms.ModelForm):
   
    class Meta:
        model = detail
        fields =('name','phone_number','location','blood_group','ward_type','doctor')

        def __init__(self,*arg,**kwargs):
            super(detail,self),__init__(*args,**kwargs)
            self.fields['ward_type'].empty_label ="Select Ward Type"


class AppointmentForm(forms.Form):
    patientId = forms.CharField(label='Enter Patient Id', max_length='15', widget= forms.TextInput(attrs={'placeholder':'Enter Patient ID'}))
    date = forms.DateField(label='Enter date For Appointment')
    time = forms.TimeField(label='Enter TIme Field')
    doctor = forms.CharField(label='Enter doctor Name')
