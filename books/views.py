from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Book
# Create your views here.


class BookListView(ListView):
    template_name = 'book/books.html'
    model = Book
    context_object_name = 'book_list'

class BookDetailView(DetailView):
    template_name = 'book/book_detail.html'
    model = Book
    context_object_name = 'book'