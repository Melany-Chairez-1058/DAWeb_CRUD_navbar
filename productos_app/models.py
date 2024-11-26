from django.db import models

class Producto(models.Model):
    id_prod = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    tipo = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    id_prov = models.IntegerField()
    id_suc = models.IntegerField()
    def __str__(self):
        return self.id_prod
