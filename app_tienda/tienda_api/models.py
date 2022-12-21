from django.db import models

# Create your models here.
#Moto
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=30, blank=False, null=False)
    marca = models.CharField(max_length=30, blank=False, null=False)
    precio = models.IntegerField()
    clasificacion = models.CharField(max_length=50, blank=False, null=False) 
    imagen = models.CharField(max_length=200, blank=False, null=False)




    def __str__(self):
        return self.__all__


