from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class EntregableFormulario(forms.Form):
    nombre = forms.CharField()
    fecha_de_entrega = forms.DateField()
    entregado = forms.BooleanField()

class BuscaCursoForm(forms.Form):
    curso = forms.CharField()

class BuscaEstudianteForm(forms.Form):
    nombre = forms.CharField(required=False)
    apellido = forms.CharField(required=False)