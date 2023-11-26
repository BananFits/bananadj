from django.db import models


class humster(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

class Kvantorium(models.Model):
    surname = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    patronymic = models.CharField(max_length=10, blank=True)
    Birthday = models.DateTimeField(max_length=15)
    is_excellent = models.BooleanField(max_length=15)
    is_not_excellent = models.BooleanField(max_length=15)


class Favourite_book_1(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=255)
    author = models.CharField(max_length=30)
    cost = models.IntegerField()
    is_interesting_or_not = models.BooleanField(default=True or False)

