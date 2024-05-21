from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('contacto/', views.contacto, name='contacto'),
    #path('reservas', views.reservas, name='reservas'),
    #path('somos', views.somos, name='somos'),
]
