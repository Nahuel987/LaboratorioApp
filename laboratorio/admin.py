from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

# Registrar los modelos


class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')  # Columnas a mostrar para Laboratorio


class DirectorGeneralAdmin(admin.ModelAdmin):
    # Columnas a mostrar para DirectorGeneral
    list_display = ('id', 'nombre', 'laboratorio')


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion',
                    'p_costo', 'p_venta')  # Columnas a mostrar para Producto


admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
