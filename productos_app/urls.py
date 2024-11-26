from django.urls import path
from productos_app import views
urlpatterns = [
    path('producto', views.inicio_vistaProducto, name='producto'),
    path("registrarProducto/",views.registrarProducto,name="registrarProducto"),
    path("seleccionarProducto/<int:id_prod>",views.seleccionarProducto,name="selecionarProducto"),
    path("editarProducto/",views.editarProducto,name="editarProducto"),
    path("borrarProducto/<int:id_prod>",views.borrarProducto,name="borrarProducto"),
]
