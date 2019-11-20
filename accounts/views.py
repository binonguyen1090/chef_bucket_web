from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'User already has been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return render(request, 'allchefs/home.html')
        else:
            return render(request, 'accounts/signup.html',{'error': 'Passowrd miss match'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')
 