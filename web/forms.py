from django import forms

class altaReservaForm(forms.forms):
    nombre = forms.CharField(label='Nombre del Reservador', required=True)
    apellido = forms.CharField(label='Apellido del Reservador', required=True)
    dni = forms.IntegerField(label='Dni', required=True)
    email = forms.EmailField(label='email',required=True )