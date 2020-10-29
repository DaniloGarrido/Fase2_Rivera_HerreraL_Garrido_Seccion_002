from django.shortcuts import render
from .models import Producto, Marca
from django.views import generic

# Create your views here.
def index(request):
    num_productos=Producto.objects.all().count()
    num_marcas=Marca.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_productos':num_productos,'num_marcas':num_marcas},
    )
