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

class Favourite_book(models.Model):
    title = models.CharField(max_length=10)
    summary = models.CharField(max_length=10)
    author = models.CharField(max_length=10)
    cost = models.CharField(max_length=15)
    is_interesting = models.BooleanField(max_length=15)
    is_not_interesting = models.BooleanField(max_length=15)
