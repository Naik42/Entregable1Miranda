from django.contrib import admin

from appNM.models import Curso, Estudiante, Profesor

# Register your models here.
admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Estudiante)
