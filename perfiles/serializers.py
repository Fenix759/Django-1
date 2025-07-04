from rest_framework import serializers
from .models import Administrador, Instructor, Ficha

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = ['id', 'nombre_admin', 'contraseña_admin', 'correo_admin']

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'nombre_instructor', 'contraseña_instructor', 'correo_instructor']
        
class FichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha
        fields = ['id', 'numero_ficha']