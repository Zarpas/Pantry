from django import forms
from .models import Ubicacion
from .models import Estante
from .models import Referencia
from .models import Alimento


class UbicacionForm(forms.ModelForm):

    class Meta:
        model = Ubicacion
        fields = ('nombre', 'descripcion', 'enUso',)


class EstanteForm(forms.ModelForm):

    class Meta:
        model = Estante
        fields = ('refUbicacion', 'nombre', 'ubicacion', 'enUso',)


class ReferenciaForm(forms.ModelForm):

    class Meta:
        model = Referencia
        fields = ('nombre', 'fabricante', 'codigoBarras', 'unidad',)


class AlimentoForm(forms.ModelForm):

    class Meta:
        model = Alimento
        fields = ('refEstante', 'refReferencia', 'cantidad', 'caducidad',)
