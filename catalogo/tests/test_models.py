from django.test import TestCase
from . models import Producto, Marca

class ProductoTestCase(TestCase):
    
    def setUp(self):
        p1=Marca.objects.create(m1="MSI")
        Producto.objects.create(nombre="GTX 1650s", marca=p1)

    def test_producto_marca(self):
        producto1= Producto.objects.get(nombre="GTX 1650s")
        self.assertEqual(producto1.marca.m1,"MSI")
        
