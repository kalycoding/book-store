from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
import uuid
# Create your models here.

class Book(models.Model):
    """ id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    ) """
    title = models.CharField(max_length=250)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers', blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )
    review = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.review
    