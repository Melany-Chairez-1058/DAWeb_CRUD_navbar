from django.db import models

# Create your models here.

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono=models.CharField(max_length=11)
    direccion=models.CharField(max_length=100)
    fecha=models.DateField(verbose_name="Fecha de Registro",null=False,blank=False)
    

    def __str__(self) :
        return self.id_cliente
    
