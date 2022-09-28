from django.contrib import admin

# Register your models here.

from .models import Language,Code



admin.site.register(Language)
admin.site.register(Code)