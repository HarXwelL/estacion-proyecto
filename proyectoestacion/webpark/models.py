from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class TipoVehiculo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Administrador(AbstractUser):
    telefono = models.CharField(max_length=9)


class Usuario(models.Model):
    nusuario = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=30, blank= False, null= False)
    correo = models.EmailField(max_length=250)
    telefono = models.CharField(max_length=9)

    def __str__(self):
        return self.nusuario

class Vehiculo(models.Model):
    nro_placa = models.CharField(max_length=14, unique=True, primary_key=True)
    marca = models.CharField(max_length=50)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_tipovehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE)
    color = models.CharField(max_length=20)
    imagen_vehiculo = models.ImageField(upload_to='vehiculos',blank=True,null=True)

    def __str__(self):
        return self.nro_placa

class Estacionamiento(models.Model):
    direccion = models.CharField(max_length=100)
    tarifa = models.DecimalField(max_digits=6,decimal_places=2)
    nombre_estac = models.CharField(max_length=50)
    nro_espacios = models.IntegerField(default=0)
    espacio_disponible = models.IntegerField(default=0)
    telefono = models.CharField(max_length=50)
    disponibilidad = models.CharField(max_length=70)
    

    def __str__(self):
        return self.nombre_estac

class Reservas(models.Model):
    id_estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
    nro_placa = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=70)
    fecha_entrada = models.DateTimeField(null=False)
    fecha_salida = models.DateTimeField(null=False)
    monto = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.descripcion