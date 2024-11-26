from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.


def inicio_vistaCliente(request):
    losclientes=Cliente.objects.all()
    return render(request,'gestionarCliente.html',{'misclientes':losclientes})
    

def registrarCliente(request):
    id_cliente =request.POST["cli"]
    nombre=request.POST["nom"]
    telefono=request.POST["tel"]
    direccion=request.POST["dir"]
    fecha=request.POST["reg"]
    guardarCliente=Cliente.objects.create(id_cliente= id_cliente,nombre=nombre,telefono=telefono,direccion=direccion,fecha=fecha)
    return redirect('cliente')

def seleccionarCliente(request,id_cliente):
    Clientes=Cliente.objects.get(id_cliente=id_cliente)
    return render(request,'editarCliente.html',{'misclientes':Clientes})

def editarCliente(request):
    id_cliente =request.POST["cli"]
    nombre=request.POST["nom"]
    telefono=request.POST["tel"]
    direccion=request.POST["dir"]
    fecha=request.POST["reg"]
    Clientes=Cliente.objects.get(id_cliente=id_cliente)
    Clientes.id_cliente=id_cliente
    Clientes.nombre=nombre
    Clientes.telefono=telefono
    Clientes.direccion=direccion
    Clientes.fecha=fecha
    
    Clientes.save()
    return redirect('cliente')
    

def borrarCliente(request,id_cliente):
    Clientes=Cliente.objects.get(id_cliente=id_cliente)
    Clientes.delete()
    return redirect('cliente')