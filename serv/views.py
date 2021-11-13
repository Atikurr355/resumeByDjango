from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    serviceData = Service.objects.all()
    context = {
        'services':"active",
        'data': serviceData
    }
    return render(request, 'serv/services.html',context)