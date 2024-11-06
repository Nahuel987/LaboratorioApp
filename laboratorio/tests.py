from django.test import TestCase
from .models import Laboratorio
from django.urls import reverse


class LaboratorioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crea un laboratorio de prueba en la base de datos
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio de Prueba",
            ciudad="Ciudad de Prueba",
            pais="País de Prueba"
        )

    def test_laboratorio_data_matches(self):
        # Obtiene el laboratorio desde la base de datos
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)

        # Verifica que los datos coinciden con los creados en setUpTestData
        self.assertEqual(laboratorio.nombre, "Laboratorio de Prueba")
        self.assertEqual(laboratorio.ciudad, "Ciudad de Prueba")
        self.assertEqual(laboratorio.pais, "País de Prueba")

    def test_laboratorio_list_url(self):
        # Obtiene la URL para la vista de lista de laboratorios
        url = reverse('laboratorio_list')

        # Realiza una solicitud GET a la URL
        response = self.client.get(url)

        # Verifica que la respuesta HTTP sea 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_laboratorio_list_page(self):
        # Obtiene la URL usando reverse por el nombre de la URL
        url = reverse('laboratorio_list')

        # Realiza una solicitud GET a la URL
        response = self.client.get(url)

        # Verifica que la respuesta HTTP sea 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verifica que se esté usando la plantilla correcta
        self.assertTemplateUsed(response, 'laboratorio/laboratorio_list.html')

        # Verifica que el contenido HTML esperado esté en la respuesta
        # Aquí puedes verificar que el nombre del laboratorio de prueba esté en el HTML
        self.assertContains(response, "Laboratorio de Prueba")
        self.assertContains(response, "Ciudad de Prueba")
        self.assertContains(response, "País de Prueba")
