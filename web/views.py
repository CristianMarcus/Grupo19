from django.shortcuts import render
from django import urls

def index(request):
  
    return render(request, 'web/index.html')

def contacto(request):
         contexto = {
             'alta_Reserva_Form': forms.altaReservaForm()
         }
         if request.method == 'POST':
          #creo la instancia del formulario con los datos cargados en pantalla
           contacto_form = contacto_form(request.POST)
           #valido y proceso los datos
         else:
            #creo el formulario vacio con los valores por defecto
          contacto_form = contacto_form()   

     
         return render(request, 'web/contacto.html', contexto)

#def reservas(request):

#    return render(request, 'web/reservas.html')

#def somos(request):

#    return render(request, 'web/somos.html')


