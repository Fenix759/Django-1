from django.db import models

# Create your models here.
class Administrador(models.Model):
    nombre_admin = models.CharField(max_length=100)
    contraseña_admin = models.CharField(max_length=100)
    correo_admin = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre_admin

class Instructor(models.Model):
    nombre_instructor = models.CharField(max_length=100)
    contraseña_instructor = models.CharField(max_length=100)
    correo_instructor = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre_instructor

class Ficha(models.Model):
    numero_ficha = models.IntegerField(unique=True)

    def __str__(self):
        return self.numero_ficha
