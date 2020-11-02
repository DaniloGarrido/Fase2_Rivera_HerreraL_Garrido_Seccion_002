from django.shortcuts import render
from .models import Producto, Marca
from django.views import generic

#Info Formularios
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):

    return render(
        request,
        'index.html',
        context={},
    )

class ProductoCreate(CreateView):
    model= Producto
    fields='__all__'

class ProductoUpdate(UpdateView):
    model=Producto
    fields=['Nombre']
    
class ProductoDelete(DeleteView):
    model=Producto
    success_url=reverse_lazy('producto')

class ProductoDetailView(generic.DetailView):
    model=Producto

class ProductoListView(generic.ListView):
    model = Producto
    paginate_by = 10
#///////////////////////
class MarcaCreate(CreateView):
    model= Marca
    fields='__all__'

class MarcaUpdate(UpdateView):
    model=Marca
    fields=['marca']
    
class MarcaDelete(DeleteView):
    model=Marca
    success_url=reverse_lazy('marca')

class MarcaDetailView(generic.DetailView):
    model=Marca

class MarcaListView(generic.ListView):
    model = Marca
    paginate_by = 10