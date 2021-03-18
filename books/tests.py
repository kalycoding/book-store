from django.test import TestCase
from .models import Book, Review
from django.contrib.auth import get_user_model, authenticate, login
from django.test.client import RequestFactory
from django.urls import reverse
from .views import BookListView, BookCreationFormView
# Create your tests here.

class BookTest(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(username = 'muhammad', email='muhammad@gmail.com', password='c9mxQKJ!T')
        
    def test_book_view(self):
        request = self.factory.get('/books/')
        request.user = self.user
        response = BookListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.template_name[0], 'teams/teams_list.html')

    def test_book_creation(self):
        request = self.factory.post('/books/new_books', {'title':'JavaScript', 'price':str(1000.00)})
        #self.assertEqual(Book.objects.last().title, "JavaScript")