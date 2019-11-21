
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('aboutchef/<chef_id>', views.aboutchef, name='aboutchef'),
    path('search', views.search, name='search'),
   
]