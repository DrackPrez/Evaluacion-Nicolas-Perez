from django import forms
from crudApp.models import Inscritos, Institucion

class FormInscritos(forms.ModelForm):
    fecha_inscripcion=forms.DateField(widget=forms.EmailInput(attrs={
            'class':'form-control mb-3',
            'type':'date'
        }),label="Fecha Inscripcion: ")
    
    hora_inscripcion = forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))
    

    class Meta:
        model = Inscritos
        fields = '__all__'


class FormInstitucion(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = '__all__'
