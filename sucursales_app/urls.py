from django.urls import path
from sucursales_app import views
urlpatterns = [
    path('sucursal', views.inicio_vistaSucursal, name='sucursal'),
    path("registrarSucursal/",views.registrarSucursal,name="registrarSucursal"),
    path("seleccionarSucursal/<id_suc>",views.seleccionarSucursal,name="selecionarSucursal"),
    path("editarSucursal/",views.editarSucursal,name="editarSucursal"),
    path("borrarSucursal/<id_suc>",views.borrarSucursal,name="borrarSucursal"),
]
