from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return self.title
    