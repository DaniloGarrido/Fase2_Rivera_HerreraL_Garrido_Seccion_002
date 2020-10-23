from django.contrib import admin

# Register your models here.
from . models import Producto, Marca

admin.site.register(Producto)
admin.site.register(Marca)