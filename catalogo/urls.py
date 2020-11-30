
from django.urls import path

from . import views
urlpatterns = [
   
    path('',views.index,name='index'),
    path('producto/<int:pk>',views.ProductoDetailView.as_view(),name='producto-detail'),
    path('productos/', views.ProductoListView.as_view(), name='producto'),
    path('marca/<int:pk>/',views.MarcaDetailView.as_view(),name='marca-detail'),
    path('marcas/', views.MarcaListView.as_view(), name='marca'),
    path('compra/<int:pk>/',views.CompraDetailView.as_view(),name='compra-detail'),
]

urlpatterns+=[ 
    path('producto/create/',views.ProductoCreate,name='producto_create'),
    path('producto/<int:pk>/update/',views.ProductoUpdate.as_view(),name='producto_update'),
    path('producto/<int:pk>/delete/',views.ProductoDelete.as_view(),name='producto_delete'),
    path('marca/create/',views.MarcaCreate.as_view(),name='marca_create'),
    path('marca/<int:pk>/update/',views.MarcaUpdate.as_view(),name='marca_update'),
    path('marca/<int:pk>/delete/',views.MarcaDelete.as_view(),name='marca_delete'),
    path('compra/create/',views.CompraCreate.as_view(),name='compra_create'),
]

