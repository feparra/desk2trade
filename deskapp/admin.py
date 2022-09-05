from atexit import register
from django.contrib import admin


from .models import Desk

class DeskAdmin(admin.ModelAdmin):
    list_display = ("Modalidad","Precio","temporalidad")

admin.site.register(Desk,DeskAdmin)

