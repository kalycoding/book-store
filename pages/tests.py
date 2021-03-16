from django.test import TestCase, SimpleTestCase
from django.urls import reverse
import requests
# Create your tests here.


class HomePageTest(SimpleTestCase):
    

    def setUp(self):
        url = '/'
        self.response = self.client.get(url)
    def test_home_page_status(self):
        
        self.assertEqual(self.response.status_code, 200)

    def test_templates(self):
        
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains(self):
        
        self.assertContains(self.response, 'Homepage')

class AboutPageTest(SimpleTestCase):
    

    def setUp(self):
        url = '/about/'
        self.response = self.client.get(url)
    def test_home_page_status(self):
        
        self.assertEqual(self.response.status_code, 200)

    def test_templates(self):
        
        self.assertTemplateUsed(self.response, 'about.html')

    def test_homepage_contains(self):
        
        self.assertContains(self.response, 'About Page')