from django.shortcuts import render
from django.db import connection


# Create your views here.
def home(request):
    
    return render(request, 'app/home.html')