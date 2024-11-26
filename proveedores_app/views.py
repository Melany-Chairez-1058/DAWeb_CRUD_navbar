from django.shortcuts import render,redirect
from .models import Proveedor
# Create your views here.

def inicio_vistaProveedor(request):
    losproveedores=Proveedor.objects.all()
    return render(request,'gestionarProveedor.html',{'misproveedores':losproveedores})
    

def registrarProveedor(request):
    id_pr=request.POST["pr"]
    nom=request.POST["nom"]
    tel=request.POST["tel"]
    cor=request.POST["cor"]
    dir=request.POST["dir"]
    stock=request.POST["st"]
    cal=request.POST["cal"]


    guardarProveedor=Proveedor.objects.create( id_pr=id_pr, nom=nom,  tel=tel,cor=cor, dir= dir,stock=stock,cal=cal)
    return redirect('proveedor')

def seleccionarProveedor(request,id_pr):
    Proveedores=Proveedor.objects.get(id_pr=id_pr)
    return render(request,'editarProveedor.html',{'misproveedores':Proveedores})

def editarProveedor(request):
    id_pr=request.POST["pr"]
    nom=request.POST["nom"]
    tel=request.POST["tel"]
    cor=request.POST["cor"]
    dir=request.POST["dir"]
    stock=request.POST["st"]
    cal=request.POST["cal"]
    Proveedores=Proveedor.objects.get(id_pr=id_pr)
    Proveedores.id_pr=id_pr
    Proveedores.nom=nom
    Proveedores.tel=tel
    Proveedores.cor=cor
    Proveedores.dir=dir
    Proveedores.stock=stock
    Proveedores.cal=cal
    
    Proveedores.save()
    return redirect('proveedor')
    

def borrarProveedor(request,id_pr):
    Proveedores=Proveedor.objects.get(id_pr=id_pr)
    Proveedores.delete()
    return redirect('proveedor')