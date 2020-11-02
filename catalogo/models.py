from django.db import models        #definir modelos
from django.urls import reverse     #direccionar los modelos a urls
import uuid                         #permite reconocer los campos clave de una clase
# Create your models here.
class Marca(models.Model):
    marca=models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse('marca-detail', args=[str(self.id)])
        
    def __str__(self):
        return f'{self.marca}' 

   
    

class Producto(models.Model):
    nombre=models.CharField(max_length=100 ,help_text='Nombre del producto')
    marca = models.ManyToManyField(Marca, help_text="Seleccione una marca para este producto")
    modelo=models.CharField(max_length=50,help_text='Modelo del producto')
    precio=models.PositiveIntegerField(blank=False,help_text='Precio del producto')
    color=models.CharField(max_length=25, null=True, blank=True,help_text='Color del producto(Puede quedar en blanco)')
    peso=models.DecimalField(decimal_places=2, max_digits=4, null=True,blank=True,help_text='Peso del producto (puede quedar en blanco)')
    alto=models.DecimalField(decimal_places=2, max_digits=4, null=True,blank=True,help_text='Alto del produscto(puede quedar en blanco)')
    ancho=models.DecimalField(decimal_places=2, max_digits=4, null=True,blank=True,help_text='Ancho del producto(puede quedar en blanco)')
    
    def get_absolute_url(self):
        return reverse('producto-detail', args=[str(self.id)])

    def __str__(self):
        return self.nombre


