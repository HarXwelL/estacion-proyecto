from io import DEFAULT_BUFFER_SIZE
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import authenticate, login
from .forms import SignupForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


from django.contrib.auth.forms import authenticate
import requests


# Create your views here.

def index(request):
    return render(request, "webpark/index.html")

def reservation(request):
    response = requests.get('https://prueba123569.herokuapp.com/estacion/reserva/').json()
    return render(request, "webpark/reservation.html", {'response' : response})

def team(request):
    return render(request, "webpark/team.html")

def user(request):
    response = requests.get('https://prueba123569.herokuapp.com/estacion/usuario').json()
    return render(request, "webpark/user.html", {'response' : response})

def login_auth(request):
    error= ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        #import pdb; pdb.set_trace()
        if user:
            login(request,user)
            error = "no"
            return redirect('index')
        else:
            error = "yes"
        
    d = {'error': error}
    return render(request, "webpark/login.html", d)



def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SignupForm()

    return render( 
        request=request,
        template_name='webpark/register.html',
        context={'form': form}
    )

@login_required
def user_logout(request):
    
    logout(request)

    return redirect('index')





def contact(request):
    estacionamiento = Estacionamiento.objects.all()
    messages.success(request, '¡Listado de estacionamientos!')
    return render(request, "webpark/contact.html", {"estacionamiento": estacionamiento})

def pago(request):
    return render(request, "webpark/pago.html")

"""def estacion(request):
    estacionamiento = Estacionamiento.objects.all()
    messages.success(request, '¡Listado de estacionamientos!')
    return render(request, "contact.html", {"estacionamiento": estacionamiento})"""

def registrarEstacion(request):
    nombre_estac = request.POST['txtEstacionamiento']
    direccion = request.POST['txtDireccion']
    tarifa = request.POST['txtTarifa']
    nro_espacios = request.POST['txtEspacios']
    espacio_disponible = request.POST['txtCapacidad']
    telefono = request.POST['txtTelefono']
    disponibilidad = request.POST['txtDisponibilidad']

    estacion = Estacionamiento.objects.create(
        nombre_estac=nombre_estac, direccion=direccion, tarifa=tarifa, nro_espacios=nro_espacios,
        espacio_disponible=espacio_disponible, telefono=telefono, disponibilidad=disponibilidad)
    estacion.save()
    return redirect('contact')

def eliminarEstacion(request, nombre_estac):
    estacion = Estacionamiento.objects.get(nombre_estac=nombre_estac)
    estacion.delete()
    messages.success(request, '¡Estacion eliminado!')
    return redirect('contact')

def editarEstacion(request, nombre_estac):
    estacion = Estacionamiento.objects.get(nombre_estac=nombre_estac)
    return render(request, "webpark/editarEstacion.html", {"estacion": estacion})


def edicionEstacion(request):
    nombre_estac = request.POST['txtEstacionamiento']
    direccion = request.POST['txtDireccion']
    tarifa = request.POST['txtTarifa']
    nro_espacios = request.POST['txtEspacios']
    espacio_disponible = request.POST['txtCapacidad']
    telefono = request.POST['txtTelefono']
    disponibilidad = request.POST['txtDisponibilidad']

    estacion = Estacionamiento.objects.get(nombre_estac=nombre_estac)
    estacion.direccion = direccion
    estacion.tarifa = tarifa
    estacion.nro_espacios = nro_espacios
    estacion.espacio_disponible = espacio_disponible
    estacion.telefono = telefono
    estacion.disponibilidad = disponibilidad
    estacion.save()
    return redirect('contact')