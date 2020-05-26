from django.shortcuts import render, redirect
from .forms import DoctorForm

def doctor_list(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('doctor_list')
        
    else:
        form = DoctorForm()
        return render(request,"doctor_form.html",{'forms':form})
