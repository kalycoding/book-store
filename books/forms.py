from django import forms
from .models import Book




class BooksCreationForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'cover']

