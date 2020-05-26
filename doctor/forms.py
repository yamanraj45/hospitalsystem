from .models import DoctorDetail

from django import forms


class DoctorForm(forms.ModelForm):
    

    class Meta:
        model = DoctorDetail
        fields=('name','location','phone_number')


        # def __init__(self, *arg, **kwargs)
        # super(self,DoctorDetail), __init__(*args,**kwargs)
