from django.urls import path
from empleados_app import views
urlpatterns = [
    path('empleado', views.inicio_vistaEmpleado, name='empleado'),
    path("registrarEmpleado/",views.registrarEmpleado,name="registrarEmpleado"),
    path("seleccionarEmpleado/<id_emp>",views.seleccionarEmpleado,name="selecionarEmpleado"),
    path("editarEmpleado/",views.editarEmpleado,name="editarEmpleado"),
    path("borrarEmpleado/<id_emp>",views.borrarEmpleado,name="borrarEmpleado"),
]
