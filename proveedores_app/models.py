from django.db import models

# Create your models here.

class Proveedor(models.Model):
    id_pr = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50, verbose_name="Nombre del Empleado")
    tel=models.CharField(max_length=11)
    cor=models.EmailField(max_length=100, verbose_name="correo")
    dir=models.CharField(verbose_name="direccion", max_length=100,null=False,blank=False)
    stock=models.BigIntegerField(verbose_name="stock")
    cal=models.PositiveSmallIntegerField( verbose_name="Calificación")
    
def __str__(self) :
        return self.id_pr
    
