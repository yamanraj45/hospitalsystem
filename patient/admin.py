from django.contrib import admin

from .models import ward
from .models import detail



admin.register(ward,detail)(admin.ModelAdmin)