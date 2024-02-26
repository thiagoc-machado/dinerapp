from django import forms
from .models import movimentos

class MovimentoForm(forms.ModelForm):
    class Meta:
        model = movimentos
        fields = ['nome', 'valor', 'categoria', 'descr', 'in_out']

        

