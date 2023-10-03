from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni = models.IntegerField()

    def __str__(self):
        return f"nombre: {self.nombre} - apellido: {self.apellido} - dni: {self.dni}"


class Producto(models.Model):
    nombre= models.CharField(max_length=40)
    numero= models.IntegerField()
    cantidad= models.IntegerField()

    def __str__(self):
        return f"nombre: {self.nombre} - numero: {self.numero} - cantidad: {self.cantidad}"
    

class Envio(models.Model):
    origen= models.CharField(max_length=40)
    destino= models.CharField(max_length=40)
    numero= models.IntegerField()
    producto= models.IntegerField() 

    def __str__(self):
        return f"origen: {self.origen} - destino: {self.destino} - numero: {self.numero} - producto: {self.producto}"


class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatar', blank=True, null=True)