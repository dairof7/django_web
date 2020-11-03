from django.contrib import admin
from .models import Servicio
# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    #agrego los campos created y updated para q sean visualizados
    readonly_fields=('created', 'updated', 'id')

admin.site.register(Servicio, ServicioAdmin)