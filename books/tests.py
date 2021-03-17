from django.test import TestCase
from .models import Book, Review
from django.contrib.auth import get_user_model
# Create your tests here.

class BookTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            email='enmaza@gmail.com',
            username='enmaza',
            password='enmaza'
        )
        self.book = Book.objects.create(
            title = 'Harry Porter',
            author = self.user,
            price = 505.45
        )

        self.review = Review.objects.create(
            book = self.book,
            author = self.user,
            review = 'Nice book'
        )
        list_url = '/books/'
        detail_url = '/books/1/'
        self.list_response = self.client.get(list_url)
        self.detail_response = self.client.get(detail_url)

    def test_book_creation(self):
        self.assertEqual(f'{self.book.title}', 'Harry Porter')
        self.assertEqual(f'{self.book.author}', self.user.username)
        self.assertEqual(f'{self.book.price}', str(505.45))

    def test_book_list_views(self):
        self.assertEqual(self.list_response.status_code, 200)
        self.assertTemplateUsed(self.list_response, 'book/books.html')

    """ def test_book_detail_views(self):
        self.assertEqual(self.detail_response.status_code, 301)
        self.assertTemplateUsed(self.detail_response, 'book/book_detail.html') """

