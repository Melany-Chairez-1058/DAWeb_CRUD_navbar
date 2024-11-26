from django.shortcuts import render,redirect
from .models import Empleado
# Create your views here.

def inicio_vistaEmpleado(request):
    losempleados=Empleado.objects.all()
    return render(request,'gestionarEmpleado.html',{'misempleados':losempleados})
    

def registrarEmpleado(request):
    id_emp=request.POST["em"]
    nombre=request.POST["nom"]
    puesto=request.POST["pues"]
    tel=request.POST["tel"]
    correo=request.POST["cor"]
    fecha_contrato=request.POST["cont"]
    salario=request.POST["sal"]


    guardarEmpleado=Empleado.objects.create( id_emp=id_emp, nombre=nombre, puesto=puesto, tel=tel, correo= correo,fecha_contrato=fecha_contrato,salario=salario)
    return redirect('empleado')

def seleccionarEmpleado(request,id_emp):
    Empleados=Empleado.objects.get(id_emp=id_emp)
    return render(request,'editarEmpleado.html',{'misempleados':Empleados})

def editarEmpleado(request):
    id_emp=request.POST["em"]
    nombre=request.POST["nom"]
    puesto=request.POST["pues"]
    tel=request.POST["tel"]
    correo=request.POST["cor"]
    fecha_contrato=request.POST["cont"]
    salario=request.POST["sal"]


    Empleados=Empleado.objects.get(id_emp=id_emp)
    Empleados.id_emp=id_emp 
    Empleados.nombre=nombre
    Empleados.puesto=puesto
    Empleados.tel=tel
    Empleados.correo=correo
    Empleados.fecha_contrato=fecha_contrato
    Empleados.salario=salario
    
    Empleados.save()
    return redirect('empleado')
    

def borrarEmpleado(request,id_emp):
    Empleados=Empleado.objects.get(id_emp=id_emp)
    Empleados.delete()
    return redirect('empleado')