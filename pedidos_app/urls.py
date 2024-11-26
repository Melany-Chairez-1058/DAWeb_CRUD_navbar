from django.urls import path
from pedidos_app import views
urlpatterns = [
    path('pedido', views.inicio_vistaPedido, name='pedido'),
    path("registrarPedido/",views.registrarPedido,name="registrarPedido"),
    path("seleccionarPedido/<id_pedido>",views.seleccionarPedido,name="selecionarPedido"),
    path("editarPedido/",views.editarPedido,name="editarPedido"),
    path("borrarPedido/<id_pedido>",views.borrarPedido,name="borrarPedido"),
]
