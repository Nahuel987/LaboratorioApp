from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

# Registrar los modelos


class LaboratorioAdmin(admin.ModelAdmin):
    # Agrega los campos ciudad y pais
    list_display = ('id', 'nombre', 'ciudad', 'pais')


class DirectorGeneralAdmin(admin.ModelAdmin):
    # Agrega el campo especialidad
    list_display = ('id', 'nombre', 'laboratorio', 'especialidad')


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio',
                    'f_fabricacion', 'p_costo', 'p_venta')


admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
