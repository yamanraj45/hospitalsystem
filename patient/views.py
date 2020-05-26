from django.shortcuts import render, redirect
from .forms import PatientForm,AppointmentForm
from .models import detail
from django.db.models import Q
from django.contrib import messages 


def appointment(request):
    form = AppointmentForm
    return render(request, 'appointment.html',{'form':form})

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

def patient_detail(request,id):
    detailpatient = detail.objects.get(pk=id)
    context = {
        "detail":detailpatient
    } 
    return render(request,'patient_detail.html',context)
    

def search(request):
    if request.method== 'GET':
        search = request.GET.get('patient_search')
        print(search)

        if search:

            match = detail.objects.filter(Q(name__icontains=search)| Q(id__icontains=search))
            if match:
                print("done")
                return render(request, 'patient_list.html',{'found':match})
            else:
                print("em")
                messages.error(request,'No Result Found')
                
        else:
            return redirect('list/')
    return render(request,'patient_list.html')