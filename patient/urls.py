from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('list/',views.patient_list,name='list'),
    path('<int:id>/',views.index, name='update'),
    path('delete/<int:id>/',views.delete, name='delete')
]