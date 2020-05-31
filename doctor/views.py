from django.shortcuts import render, redirect
from .forms import DoctorForm
from patient.forms import AppointmentForm
from patient.models import detail
from django.contrib import messages 
from django.db.models import Q


def doctor_list(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('doctor_list')
        
    else:
        form = DoctorForm()
        return render(request,"doctor_form.html",{'forms':form})



def appointment(request):
    return render(request, 'appointment.html',{'appointment':AppointmentForm})



def search(request):
    if request.method== 'GET':
        search = request.GET.get('checkpatientid')
        

        if search:
            
            print(search)

            match = detail.objects.filter(Q(id__exact=search))
            if match:
                contextsearch={
                    'appointment' : AppointmentForm,
                    'found':match
                }
                print(match)
                print("done")  #working upto here//// the line below is showing error
                return render(request,'appointment.html',contextsearch)
            else:
                print('error')
                messages.error(request,'No Result Found')
                
        else:
            print("donssse")
            return redirect('checkpatientid')
    return render(request,'appointment.html',{'appointment':AppointmentForm})