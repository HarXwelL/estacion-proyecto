from django.contrib import admin

# Register your models here.
from .models import TipoVehiculo
from .models import Administrador
from .models import Usuario
from .models import Vehiculo
from .models import Estacionamiento
from .models import Reservas

admin.site.register(TipoVehiculo)
admin.site.register(Administrador)
admin.site.register(Usuario)
admin.site.register(Estacionamiento)
admin.site.register(Vehiculo)
admin.site.register(Reservas)