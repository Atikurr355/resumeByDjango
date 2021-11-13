from django.contrib import admin
from .models import Home
# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("core/css/core.css",)
        }

        js = ("core/js/home.js",)

admin.site.register(Home,HomeAdmin)