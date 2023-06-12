from django import forms
from .models import Cliente, Mascota, HistoriaClinica

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__' 


class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = '__all__'  
