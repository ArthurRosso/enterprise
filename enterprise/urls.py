from django.urls.conf import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # URL padrão
    path('', include('skymap.urls', namespace='skymap')),

    # Interface administrativa
    path('admin/', admin.site.urls),
]