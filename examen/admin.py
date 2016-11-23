from django.contrib import admin
from .models import Usuario, Marca,MarcaAdmin, Producto,ProductoAdmin, Venta, VentaAdmin

admin.site.register(Usuario)
admin.site.register(Marca,MarcaAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Venta, VentaAdmin)
