from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('list/',views.patient_list,name='list'),
    path('<int:id>/',views.index, name='update'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('patientdetail/<int:id>',views.patient_detail,name='patient_detail'),
    path('search/',views.search,name='search'),
    path('appointment/',views.appointment, name='appoint'),
    path('future/',views.futurehomepage,name='homepage')
]