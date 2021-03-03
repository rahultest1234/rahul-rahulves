from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
    
    def test_http_response(self):
        url = reverse('a1:index')
        response = self.client.get(url+'?user_name=hello')
        print(str(response.content))
        self.assertEqual(response.content.decode('utf-8'), "Hello, My Name is hello")
