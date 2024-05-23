from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def logeo(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ingreso')  # Redirige a la vista de ingreso
            else:
                form.add_error(None, "Username or password is incorrect")
    else:
        form = LoginForm()  # Inicializa el formulario aquí solo si el método no es POST

    return render(request, 'web/logeo.html', {'form': form})

def ingreso_view(request):
    return render(request, 'web/ingreso.html')

def index(request):
    return render(request, 'web/index.html')

def contacto(request):
    return render(request, 'web/contacto.html')

def somos(request):
    return render(request, 'web/somos.html')

def reserva(request):
    return render(request, 'web/reservas.html')






