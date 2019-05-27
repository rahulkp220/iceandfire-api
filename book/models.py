from datetime import datetime
from django.db import models


# Author model
class Author(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


# Book model
class Book(models.Model):
    name = models.CharField(max_length=120, unique=True)
    isbn = models.CharField(max_length=40)
    authors = models.ManyToManyField(Author)
    country = models.CharField(max_length=80)
    number_of_pages = models.PositiveIntegerField()
    publisher = models.CharField(max_length=80)
    release_date = models.DateField()

    def __str__(self):
        return self.name
