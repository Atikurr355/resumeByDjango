from django.shortcuts import render
from .models import Home

# Create your views here.
def home(request):
    homeData = Home.objects.all()[0]
    context = {
        'home':"active",
        'homeData': homeData
    }
    return render(request, 'core/home.html',context)

def contacts(request):
    context = {
        'contacts':"active"
    }
    return render(request, 'core/contacts.html',context)
