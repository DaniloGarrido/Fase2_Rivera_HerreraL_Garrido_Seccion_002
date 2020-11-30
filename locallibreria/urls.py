from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from catalogo import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogo/',include('catalogo.urls')),
    path ('accounts/', include('django.contrib.auth.urls')),
    #path(r'^catalogo/', include('catalogo.urls')),
    
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)