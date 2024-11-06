from django.utils import timezone
from django.db import models


class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)  # Nuevo campo
    pais = models.CharField(max_length=255)    # Nuevo campo

    def __str__(self):
        return f"{self.nombre}"


class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=255)  # Nuevo campo

    def __str__(self):
        return f"{self.nombre} - {self.laboratorio}"


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(default=timezone.now)
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.nombre}"
