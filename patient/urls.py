from django.urls import path
from . import views
from doctor import views as dviews

urlpatterns=[
    
    path('formpatient',views.form_patient,name='form_patient'),
    path('list/',views.patient_list,name='list'),
    path('<int:id>/',views.form_patient, name='update'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('patientdetail/<int:id>',views.patient_detail,name='patient_detail'),
    path('search/',views.search,name='search'),
    path('appointment/',dviews.appointment, name='appoint'),
    path('',views.futurehomepage,name='index')
]