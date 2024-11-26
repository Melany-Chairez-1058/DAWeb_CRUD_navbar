from django.db import models

# Create your models here.

class Sucursal(models.Model):
    id_suc = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Sucursal")
    dire = models.CharField(max_length=100, verbose_name="Direccion de la Sucursal")
    horario = models.TimeField() 
    tel=models.CharField(max_length=100,verbose_name="telefono",null=False,blank=False)
    correo=models.EmailField(max_length=100,verbose_name="correo",null=False,blank=False)
    

    def __str__(self) :
        return self.id_suc
    
