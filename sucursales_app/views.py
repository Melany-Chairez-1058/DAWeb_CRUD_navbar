from django.shortcuts import render,redirect
from .models import Sucursal
# Create your views here.

def inicio_vistaSucursal(request):
    lassucursales=Sucursal.objects.all()
    return render(request,'gestionarSucursal.html',{'missucursales':lassucursales})
    
    
def registrarSucursal(request):
    id_suc=request.POST["suc"]
    nombre =request.POST["nom"]
    dire= request.POST["dire"]
    horario=request.POST["hor"]
    tel=request.POST["tel"]
    correo=request.POST["cor"]
    guardarSucursal=Sucursal.objects.create(id_suc=id_suc,nombre=nombre,dire=dire,horario=horario,tel=tel,correo=correo)
    
    return redirect('sucursal')


def seleccionarSucursal(request,id_suc):
    Sucursales=Sucursal.objects.get(id_suc=id_suc)
    return render(request,'editarSucursal.html',{'missucursales':Sucursales})


def editarSucursal(request):
    id_suc=request.POST["suc"]
    nombre =request.POST["nom"]
    dire= request.POST["dire"]
    horario=request.POST["hor"]
    tel=request.POST["tel"]
    correo=request.POST["cor"]
    Sucursales=Sucursal.objects.get(id_suc=id_suc)
    Sucursales.id_suc=id_suc
    Sucursales.nombre=nombre
    Sucursales.dire=dire
    Sucursales.horario=horario
    Sucursales.tel=tel
    Sucursales.correo=correo
    
    Sucursales.save()
    return redirect('sucursal')
    

def borrarSucursal(request,id_suc):
    Sucursales=Sucursal.objects.get(id_suc=id_suc)
    Sucursales.delete()
    return redirect('sucursal')