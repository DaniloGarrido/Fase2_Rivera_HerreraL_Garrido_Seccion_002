from django.shortcuts import render,redirect,get_object_or_404
from .models import Producto,Marca,Compra
from django.views import generic
from .  forms import ProductoForm
from django.http import HttpResponseRedirect

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

#class ProductoCreate(CreateView):
    #model= Producto
    #fields='__all__'

class ProductoUpdate(UpdateView):
    model=Producto
    fields=['nombre','marca','modelo','precio','color','peso','alto','ancho']
    
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
    fields=['marca','disponible']
    
class MarcaDelete(DeleteView):
    model=Marca
    success_url=reverse_lazy('marca')

class MarcaDetailView(generic.DetailView):
    model=Marca

class MarcaListView(generic.ListView):
    model = Marca
    paginate_by = 10
    #///////////////////////
class CompraCreate(CreateView):
    model= Compra
    fields='__all__'
class CompraDetailView(generic.DetailView):
    model=Compra



def ProductoCreate(request):
    if request.method == "post":
        form = ProductoForm(request.POST,files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #form.save_m2m()
            return HttpResponseRedirect(reverse_lazy('producto-detail'), pk=post.pk)

     

    else:
        form = ProductoForm()
        return render(request, 'catalogo/producto_form.html', {'form': form})

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from catalogo.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]