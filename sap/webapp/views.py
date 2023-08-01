from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenido(request):
    #con .objects nos conectamos a la base de datos
    no_personas = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    mensajes = {
        'msg1':'Valor mensaje 1',
        'msg2':'Valor mensaje 2',
        'no_personas':no_personas,
        'personas':personas
    }
    return render(request, 'bienvenido.html', mensajes)

