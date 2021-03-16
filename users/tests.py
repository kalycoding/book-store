from django.test import TestCase
from django.contrib.auth import get_user_model
import requests
# Create your tests here.


class CustomUserTest(TestCase):

    def setUp(self):
        self.User = get_user_model()
        self.response = self.client.get('/')
    def test_create_user(self):
        
        user = self.User.objects.create_user(
            username='kalyfacloud',
            email='kalycodes@gmail.com',
            password='c9mxQKJ*!T'
        )

        self.assertEqual(user.username, 'kalyfacloud')
        self.assertEqual(user.first_name, '')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
    
    def test_super_user(self):
        
        user = self.User.objects.create_superuser(
            username='kalycoding',
            password='c9mxQKJ*!T'
        )

        self.assertEqual(user.username, 'kalycoding')
        self.assertTrue(len(user.email)==0)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)

class SignUpPageTest(TestCase):
    def setUp(self):
        self.user = get_user_model()
        self.response = self.client.get('/accounts/signup/')

    """ def test_signup_page(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, 'About Page') """

    def test_signup_form(self):
        user = self.user.objects.create_user(
            username='kalycodes',
            email='kalycodes@gmail.com',
            password='c9mxQKJ!T'
        )

        self.assertEqual(self.user.objects.all()[0].username, user.username)