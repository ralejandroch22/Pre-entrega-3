from django.contrib import admin
from .models import *

class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre","camada",)
    list_filter = ("nombre","camada",)
    ordering = ("nombre","camada",)

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("nombre","apellido","email",)
    list_filter = ("nombre","apellido","email",)
    ordering = ("nombre","apellido","email",)

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("nombre","apellido","email",)
    list_filter = ("nombre","apellido","email",)
    ordering = ("nombre","apellido","email",)

class EntregableAdmin(admin.ModelAdmin):
    list_display = ("nombre","fecha_de_entrega","entregado")
    list_filter = ("nombre","fecha_de_entrega","entregado")
    ordering = ("nombre","fecha_de_entrega","entregado")

admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Entregable, EntregableAdmin)
