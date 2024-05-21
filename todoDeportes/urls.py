# todoDeportes/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/', include('web.urls')),  # Incluye las URLs de la app 'web'
]
