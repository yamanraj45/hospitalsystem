from django.contrib import admin

from .models import ward
from .models import detail, appointment



admin.register(ward,detail, appointment)(admin.ModelAdmin)