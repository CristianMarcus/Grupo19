# web/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define una ruta para la vista 'index'
    path('contacto/', views.contacto, name='contacto'),
    path('somos/', views.somos, name='somos'),
    path('reservas/', views.reserva, name='reservas'),
]
