from django.db import models
from django.db.models.signals import post_delete
from django.utils import timezone
from django.dispatch import receiver
from django.contrib import admin
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator


class Usuario(models.Model):
    DPI  =   models.CharField(max_length=30)
    nombre =   models.CharField(max_length=50)
    def __str__(self):
        return self.DPI

class Marca(models.Model):
    nombre  =   models.CharField(max_length=40)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo    = models.CharField(max_length=7)
    nombre    = models.CharField(max_length=60)
    foto = models.ImageField(upload_to='fotos/')
    marca   = models.ManyToManyField(Marca, through='Actuacion')
    precio = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    existencia = models.IntegerField()
    def __str__(self):
        return '%s %s' % (self.nombre, self.codigo)

class Venta(models.Model):
    DPI   = models.ManyToManyField(Usuario, through='ActuacionVenta')
    producto   = models.ManyToManyField(Producto, through='ActuacionVenta')
    cantidad = models.IntegerField()
    fecha_venta= models.DateTimeField(default=timezone.now)

class Actuacion (models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class ActuacionVenta (models.Model):
    DPI = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)


class ActuacionInLine(admin.TabularInline):
    model = Actuacion
    extra = 1

class ActuacionInLineVenta(admin.TabularInline):
    model = ActuacionVenta
    extra = 1

class MarcaAdmin(admin.ModelAdmin):
    inlines = (ActuacionInLine,)

class UsuarioAdmin(admin.ModelAdmin):
    inlines = (ActuacionInLineVenta,)


class ProductoAdmin (admin.ModelAdmin):
    inlines = (ActuacionInLine,)

class VentaAdmin (admin.ModelAdmin):
    inlines = (ActuacionInLineVenta,)
