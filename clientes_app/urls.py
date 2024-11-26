from django.urls import path
from clientes_app import views
urlpatterns = [
    path('cliente', views.inicio_vistaCliente, name='cliente'),
    path("registrarCliente/",views.registrarCliente,name="registrarCliente"),
    path("seleccionarCliente/<id_cliente>",views.seleccionarCliente,name="selecionarCliente"),
    path("editarCliente/",views.editarCliente,name="editarCliente"),
    path("borrarCliente/<id_cliente>",views.borrarCliente,name="borrarCliente"),
]
