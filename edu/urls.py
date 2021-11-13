from django.urls import path
from . import views

urlpatterns = [
    # path('services', views.services, name="services"),
    path('skills', views.skills, name="skills"),
    # path('contacts', views.contacts, name="contacts"),
]
