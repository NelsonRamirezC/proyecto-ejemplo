# example/views.py
from datetime import datetime
# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    contexto = {}
    
    return render(request, "index.html", contexto)