from django.shortcuts import render
from .models import Desk

def index(request):
    desks = Desk.objects.all()
    ctx = {'desks': desks}
    return render (request,'deskapp/index.html',ctx)
