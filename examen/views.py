from django.utils import timezone
from django.shortcuts import render
from django.contrib import messages
from .forms import PeliculaForm
from examen.models import Venta,Producto,Usuario,Marca,ActuacionVenta

def examen_nueva(request):
    if request.method == "POST":
        formulario = PeliculaForm(request.POST)
        if formulario.is_valid():
            pelicula = Venta.objects.create(DPI=formulario.cleaned_data['DPI'],cantidad = formulario.cleaned_data['cantidad'],fecha_venta = formulario.cleaned_data['fecha_venta'])
            for venta_id in request.POST.getlist('productos'):
                actuacion = ActuacionVenta(venta_id = venta_id, producto_id = pelicula.id)
                actuacion.save()
            messages.add_message(request, messages.SUCCESS, 'Guardada Exitosamente')
    else:
        formulario = PeliculaForm()
    return render(request, 'examen/pelicula_editar.html', {'formulario': formulario})
