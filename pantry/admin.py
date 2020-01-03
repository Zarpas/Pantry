from django.contrib import admin
from .models import Ubicacion
from .models import Estante
from .models import Referencia
from .models import Alimento


# Register your models here.

admin.site.register(Ubicacion)
admin.site.register(Estante)
admin.site.register(Referencia)
admin.site.register(Alimento)
