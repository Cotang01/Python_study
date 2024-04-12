from django.db import models
from random import randint


class Author(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(max_length=30, blank=False, null=False)
    avatar = models.ImageField(upload_to='images/',
                               default=f'pfp{randint(1, 1_000_000)}.png')
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} - {self.name} - {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)
    content = models.TextField(max_length=500, blank=False, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk} - {self.title}. Author: {self.author}'
