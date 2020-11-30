from django.db import models       #definir modelos
from django.urls import reverse     #direccionar los modelos a urls
import uuid                         #permite reconocer los campos clave de una clase
# Create your models here.
class Marca(models.Model):
    marca=models.CharField(max_length=100)
    disponible  = models.BooleanField(null=True)
    def get_absolute_url(self):
        return reverse('marca-detail', args=[str(self.id)])
        
    def __str__(self):
        return f'{self.marca}' 

   
    

class Producto(models.Model):
    nombre=models.CharField(max_length=100 ,help_text='Nombre del producto')
    marca = models.ForeignKey('Marca', help_text="Seleccione una marca para este producto", on_delete=models.SET_NULL,null=True,blank=True)
    modelo=models.CharField(max_length=50,help_text='Modelo del producto')
    precio=models.PositiveIntegerField(blank=False,help_text='Precio del producto')
    color=models.CharField(max_length=25, null=True, blank=True,help_text='Color del producto(Puede quedar en blanco)')
    peso=models.DecimalField(decimal_places=2, max_digits=4, null=True,blank=True,help_text='Peso del producto (puede quedar en blanco)')
    alto=models.DecimalField(decimal_places=2, max_digits=4, null=True,blank=True,help_text='Alto del producto(puede quedar en blanco)')
    ancho=models.DecimalField(decimal_places=2, max_digits=4, null=True,blank=True,help_text='Ancho del producto(puede quedar en blanco)')
    img1=models.ImageField( verbose_name="Imagen", upload_to="productos" ,null=True,blank=True)
    img2=models.ImageField( verbose_name="Imagen", upload_to="images", null=True,blank=True)
    img3=models.ImageField( verbose_name="Imagen", upload_to="images", null=True,blank=True)
    img4=models.ImageField( verbose_name="Imagen", upload_to="images", null=True,blank=True)

    def get_absolute_url(self):
        return reverse('producto-detail', args=[str(self.id)])

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    producto=models.ForeignKey('Producto', on_delete=models.SET_NULL,null=True,blank=True)
    nombre=models.CharField(max_length=100 ,help_text='Nombre completo')
    run=models.CharField(max_length=100 ,help_text='Ingrese run')
    cantidad=models.PositiveIntegerField(blank=False,help_text='Ingrese cantidad')
    telefono=models.PositiveIntegerField(blank=False,help_text='Ingrese teléfono de contacto')
    correo=models.CharField(max_length=25, null=True, blank=True,help_text='Correo')

    img1=models.ImageField( verbose_name="Imagen", upload_to="images" ,null=True,blank=True)
    LOAN_STATUS = (
        ('d', 'Default'),
        ('c', 'Custom'),
    )
    tipo = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='d',

    )
    def get_absolute_url(self):
        return reverse('compra-detail', args=[str(self.id)])
    def __str__(self):
        return self.nombre

