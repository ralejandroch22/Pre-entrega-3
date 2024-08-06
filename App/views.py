from django.shortcuts import render

from App.models import *

from App.forms import *

def inicio(request):
    return render(request, "App/index.html")

def buscar(request):
    if request.method == "POST":
        miFormulario = BuscaCursoForm(request.POST) 

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "App/mostrar_cursos.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()

    return render(request, "App/buscar_curso.html", {"miFormulario": miFormulario})

def cursos(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST) 
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()

        mi_Busqueda = BuscaCursoForm()
            #return render(request, "App/index.html")
    else:
        mi_formulario = CursoFormulario()

    cursos = Curso.objects.all()
    return render(request, "App/cursos.html", {"mi_formulario": mi_formulario, "cursos": cursos})

def profesores(request):
    if request.method == "POST":
        mi_formulario = ProfesorFormulario(request.POST) 
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            profesor.save()

            #return render(request, "App/index.html")
    else:
        mi_formulario = ProfesorFormulario()
    profesores = Profesor.objects.all()
    return render(request, "App/profesores.html", {"mi_formulario": mi_formulario, "profesores": profesores})

def estudiantes(request):
    if request.method == "POST":
        mi_formulario = EstudianteFormulario(request.POST) 
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            estudiante.save()

            #return render(request, "App/index.html")
    else:
        mi_formulario = EstudianteFormulario()
    
    estudiantes = Estudiante.objects.all()
    return render(request, "App/estudiantes.html", {"mi_formulario": mi_formulario, "estudiantes": estudiantes})

def entregables(request):
    if request.method == "POST":
        mi_formulario = EntregableFormulario(request.POST) 
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            entregable = Entregable(nombre=informacion["nombre"], fecha_de_entrega=informacion["fecha_de_entrega"], entregado=informacion["entregado"])
            entregable.save()

            #return render(request, "App/index.html")
    else:
        mi_formulario = EntregableFormulario()
    
    entregables = Entregable.objects.all()
    return render(request, "App/entregables.html", {"mi_formulario": mi_formulario, "entregables": entregables})