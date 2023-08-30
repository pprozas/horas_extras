from django.contrib import admin

# Register your models here.

from .models import Usuarios, HorasExtras

admin.site.register(Usuarios)
admin.site.register(HorasExtras)