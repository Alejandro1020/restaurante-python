
from django import forms

class FormularioEmpleados(forms.Form):

    TRABAJADOR=(
        (1,'Chef'),
        (2,'Auxiliar de cocina'),
        (3,'Administrador')

    )

    nombre=forms.CharField(
        required=True,
        max_length=5,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
   
    fotografia=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
        
    )
    salario=forms.CharField(
        required=True,
        max_length=20,    
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})

    )
    tipo=forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        choices=TRABAJADOR
    )
    perfil=forms.CharField(
        required=False,
        max_length=20,
        widget=forms.Textarea(attrs={'class':'form-control mb-3'})
    )