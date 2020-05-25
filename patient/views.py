from django.shortcuts import render, redirect
from .forms import PatientForm
from .models import detail

def index(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PatientForm()
        else:
            patient = detail.objects.get(pk=id)
            form = PatientForm(instance = patient)
        return render(request,'index.html',{'form':form})

    else:
        if id==0:
            form = PatientForm(request.POST)
        else:
            patient = detail.objects.get(pk=id)
            form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
        return redirect('/list')


def patient_list(request):
    context = {
        'patientdetails': detail.objects.all()
    }
    return render(request,'patient_list.html',context)


def delete(request,id):
    patient = detail.objects.get(pk=id)
    patient.delete()
    return redirect('/list/')
    