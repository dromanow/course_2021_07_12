from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Book(models.Model):
    name = models.CharField(max_length=64)
    authors = models.ManyToManyField(Author)


class Biography(models.Model):
    text = models.CharField(max_length=64)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
