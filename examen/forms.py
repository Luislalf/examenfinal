
from django import forms
from .models import Venta, Producto, Usuario, Marca, ActuacionVenta

class PeliculaForm(forms.ModelForm):

    class Meta:
        model = Venta
        fields = ('cantidad', 'fecha_venta', 'DPI','productos')

    def __init__ (self, *args, **kwargs):
    	super(PeliculaForm, self).__init__(*args, **kwargs)
    	self.fields["productos"].widget = forms.widgets.CheckboxSelectMultiple()
    	self.fields["productos"].queryset = Producto.objects.all()
