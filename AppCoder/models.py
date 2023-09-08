from django.db import models

class Cliente(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni = models.IntegerField()

    def __str__(self):
        return f"nombre: {self.nombre} - apellido: {self.apellido} - dni: {self.dni}"

class Producto(models.Model):
    nombre= models.CharField(max_length=30)
    numero= models.IntegerField()
    cantidad= models.IntegerField()

    def __str__(self):
        return f"nombre: {self.nombre} - numero: {self.numero} - cantidad: {self.cantidad}"
    

class Envio(models.Model):
    origen= models.CharField(max_length=30)
    destino= models.CharField(max_length=30)
    numero= models.IntegerField()
    producto= models.IntegerField() 

    def __str__(self):
        return f"origen: {self.origen} - destino: {self.destino} - numero: {self.numero} - producto: {self.producto}"
