from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        'home':"active"
    }
    return render(request, 'core/home.html',context)

def contacts(request):
    context = {
        'contacts':"active"
    }
    return render(request, 'core/contacts.html',context)
