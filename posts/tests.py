from django.test import TestCase, Client
from django.urls import reverse
class HelloViewTestCase(TestCase):
    def setup(self):
        self.client = Client()

def test_hello_view(self):
    response = self.client.get(reverse("hello"))
    expect_data = "GeekTech"
    self.assertEqual(response.status_code,200)
    
    # self.assertEqual(response.status_code,200)