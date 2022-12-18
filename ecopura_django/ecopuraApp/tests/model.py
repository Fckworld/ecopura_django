from django.test import TestCase
from django.urls import reverse
from ecopuraApp.models import Pago, Producto, Categoria, Tipo
from ecopuraApp.views import Agua


class TestAppModels(TestCase):
    def setUp(self):
        self.list_url = reverse('ecopuraApp:agua_url')

        categoria1 = Categoria.objects.create(id=1, nombre='Agua')
        categoria2 = Categoria.objects.create(id=2, nombre='Planes')
        categoria3 = Categoria.objects.create(id=3, nombre='Kit Iniciales')
        tipo1 = Tipo.objects.create(id=1, nombre='Producto')
        tipo2 = Tipo.objects.create(id=2, nombre='Servicio')
        producto1 = Producto.objects.create(
            id=1, nombre='PRODUCTO_1', precio=11111, descripcion='PRODUCTO DE PRECIO 1', categoria=categoria1, tipo=tipo1)
        producto2 = Producto.objects.create(
            id=2, nombre='PRODUCTO_2', precio=22222, descripcion='PRODUCTO DE PRECIO 2', categoria=categoria2, tipo=tipo1)
        producto3 = Producto.objects.create(
            id=3, nombre='PRODUCTO_3', precio=33333, descripcion='PRODUCTO DE PRECIO 3', categoria=categoria2, tipo=tipo2)

        producto4 = Producto.objects.create(
            id=4, nombre='PRODUCTO_4', precio=44444, descripcion='PRODUCTO DE PRECIO 4', categoria=categoria1, tipo=tipo1)
        producto5 = Producto.objects.create(
            id=5, nombre='PRODUCTO_5', precio=55555, descripcion='PRODUCTO DE PRECIO 5', categoria=categoria1, tipo=tipo1)
        producto6 = Producto.objects.create(
            id=6, nombre='PRODUCTO_6', precio=66666, descripcion='PRODUCTO DE PRECIO 6', categoria=categoria2, tipo=tipo1)

    def test_model_Pago(self):
        medio = Pago.objects.create(id=1, medio='Credito')
        self.assertEqual(str(medio), 'Credito')

    def test_list_agua_products_GET(self):
        response = self.client.get(self.list_url)
        values = Producto.objects.filter(tipo_id=1)
        qs = response.context['productos']
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'agua.html')
        self.assertQuerysetEqual(qs, values)
