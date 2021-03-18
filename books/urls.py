from django.urls import path
from .views import BookListView, BookDetailView, BookCreationFormView

urlpatterns = [
    path('', BookListView.as_view(), name='books'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('new_book/', BookCreationFormView.as_view(), name='new_book')
]
