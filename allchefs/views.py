from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Chef
# Create your views here.

def home(request):

    allchefs = Chef.objects.all
    return render(request, 'allchefs/home.html', {'allchefs' : allchefs})

def about(request):
    return render(request, 'allchefs/about.html')

    
def aboutchef(request, chef_id):
    chef_id = Chef.objects.get(pk=chef_id)
    allchefs = Chef.objects.all
    return render (request, 'allchefs/aboutchef.html', {'chef_id': chef_id})

def search(request):
    q = request.GET['q']
    if not q:
        return redirect('home')
    else:
        allchefs = Chef.objects.filter(name__icontains=q)
        if not allchefs:
            return render (request, 'allchefs/result.html', {'error': 'No search results'} )
        else:
            return render (request, 'allchefs/result.html', {'q': q,'allchefs': allchefs} )

     