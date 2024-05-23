from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('somos/', views.somos, name='somos'),
    path('reservas/', views.reserva, name='reservas'),
    path('logeo/', views.logeo, name='logeo'),
    path('ingreso/', views.ingreso_view, name='ingreso'),
]

