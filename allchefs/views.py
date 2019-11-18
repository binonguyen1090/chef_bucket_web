from django.shortcuts import render
from django.http import HttpResponse
from .models import Chef
# Create your views here.

def home(request):
    allchefs = Chef.objects.all
    return render(request, 'allchefs/home.html', {'allchefs' : allchefs})

def about(request):
    return render(request, 'allchefs/about.html')
