from django.db import models
from .choices import estados

# Create your models here.

class Institucion(models.Model):
    id= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=30)
    

    class Meta:  
        verbose_name = 'Institucion'
        verbose_name_plural = 'Instituciones'

    def __str__(self):
        return self.nombre



class Inscritos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField( max_length=50)
    telefono =models.CharField(max_length=15)
    fecha_inscripcion =models.DateField() 
    institucion = models.ForeignKey(Institucion,null=True,blank=True,on_delete=models.CASCADE)
    hora_inscripcion=models.TimeField()
    estado = models.CharField(max_length=20, choices=estados, default='No Asisten')
    observacion = models.CharField( max_length=100,blank=True)




