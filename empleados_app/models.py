from django.db import models

# Create your models here.

class Empleado(models.Model):
    id_emp = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name="Nombre del Empleado")
    puesto=models.CharField(max_length=50,verbose_name="Puesto ",null=False,blank=False)
    tel=models.CharField(max_length=11)
    correo=models.EmailField(max_length=100, verbose_name="correo")
    fecha_contrato=models.DateField(verbose_name="Fecha de contratacion",null=False,blank=False)
    salario=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Salario")

    def __str__(self) :
        return self.id_emp
    
