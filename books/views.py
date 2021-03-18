from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Book
from .forms import BooksCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin, PermissionDenied, LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.


class BookListView(LoginRequiredMixin,ListView):
    template_name = 'book/books.html'
    model = Book
    context_object_name = 'book_list'
    
    

class BookDetailView(LoginRequiredMixin,DetailView):
    template_name = 'book/book_detail.html'
    model = Book
    context_object_name = 'book'


class BookCreationFormView(LoginRequiredMixin,CreateView):
    form_class = BooksCreationForm
    success_url = reverse_lazy('books')
    template_name = 'book/new_book.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin,UpdateView):
    model = Book
    template_name = 'book/book_edit.html'
    fields = ['title', 'price', 'cover']

    def dispatch(self, request):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request)

class BookDeleteView(LoginRequiredMixin,DeleteView):
    model = Book
    template_name = 'book/book_delete.html'
    success_url = reverse_lazy('books')

    def dispatch(self, request):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request)