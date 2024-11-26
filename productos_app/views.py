from django.shortcuts import render,redirect
from .models import Producto
# Create your views here.
def inicio_vistaProducto(request):
    losproductos=Producto.objects.all()
    return render(request,'gestionarProducto.html',{'misproductos':losproductos})

def registrarProducto (request):
    id_prod=request.POST["idp"]
    precio=request.POST["precio"]
    stock=request.POST["stock"]
    descripcion=request.POST["desc"]
    tipo=request.POST["tipo"]
    categoria=request.POST["cate"]
    nombre=request.POST["nombre"]
    id_suc=request.POST["suc"]
    id_prov=request.POST["prov"]
   
    
    guardarProducto=Producto.objects.create(id_prod= id_prod,precio=precio,stock=stock,descripcion=descripcion,
     tipo=tipo,categoria=categoria,nombre=nombre,id_prov=id_prov,id_suc=id_suc)
    return redirect('producto')

def seleccionarProducto(request,id_prod):
    Productos=Producto.objects.get( id_prod= id_prod)
    return render(request,'editarProducto.html',{'misproductos':Productos})

def editarProducto(request):
    
    id_prod=request.POST["idp"]
    precio=request.POST["precio"]
    stock=request.POST["stock"]
    descripcion=request.POST["desc"]
    tipo=request.POST["tipo"]
    categoria=request.POST["cate"]
    nombre=request.POST["nombre"]
    id_suc=request.POST["suc"]
    id_prov=request.POST["prov"]
   
    Productos=Producto.objects.get(id_prod=id_prod)
    Productos.id_prod= id_prod
    Productos.precio=precio
    Productos.stock=stock
    Productos.descripcion=descripcion
    Productos.tipo=tipo
    Productos.categoria=categoria
    Productos.nombre=nombre
    Productos.id_prov=id_prov
    Productos.id_suc=id_suc
    Productos.save()
    return redirect('producto')
    
    
def borrarProducto(request,id_prod):
    Productos=Producto.objects.get(id_prod=id_prod)
    Productos.delete()
    return redirect('producto')