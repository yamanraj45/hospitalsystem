from django.shortcuts import render, redirect
from .forms import PatientForm,AppointmentForm
from .models import detail
from .models import appointment as ap
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
    
    
    appointment_detail= ap.objects.filter(patient_name=detailpatient)
    print(appointment_detail)
    context = {
        "detail":detailpatient,
        "appointments":appointment_detail
        
    } 
    return render(request,'patient_detail.html',context)
    

def search(request):
    if request.method== 'GET':
        search = request.GET.get('patient_search')
        

        if search:

            match = detail.objects.filter(Q(name__icontains=search)| Q(id__icontains=search))
            if match:
                contextsearch={
                    'found':match
                }
                print(match)
                print("done")  #working upto here//// the line below is showing error
                return render(request,'patient_list.html',contextsearch)
            else:
                
                messages.error(request,'No Result Found')
                
        else:
            return redirect('list/')
    return render(request,'patient_list.html')

def futurehomepage(request):
    return render(request,'homepage.html')