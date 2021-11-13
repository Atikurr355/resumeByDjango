from django.contrib import admin
from .models import Service
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("serv/css/serv.css",)
        }

        js = ("serv/js/serv.js",)

admin.site.register(Service,ServiceAdmin)