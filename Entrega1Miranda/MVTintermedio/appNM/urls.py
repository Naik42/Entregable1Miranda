from django.urls import path

from . import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('nuevoalumno' , views.nuevoalumno, name="NuevoAlumno"),
    path('nuevoprofe' , views.nuevoprofe, name="NuevoProfe"),
    path('nuevocurso', views.nuevocurso, name="NuevoCurso"),
    path('buscarcurso', views.busquedacurso, name="BusquedaCurso"),
    path('buscar/', views.buscar, name="Buscar"),
]