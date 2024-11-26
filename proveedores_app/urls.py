from django.urls import path
from proveedores_app import views
urlpatterns = [
    path('proveedor', views.inicio_vistaProveedor, name='proveedor'),
    path("registrarProveedor/",views.registrarProveedor,name="registrarProveedor"),
    path("seleccionarProveedor/<id_pr>",views.seleccionarProveedor,name="selecionarProveedor"),
    path("editarProveedor/",views.editarProveedor,name="editarProveedor"),
    path("borrarProveedor/<id_pr>",views.borrarProveedor,name="borrarProveedor"),
]
