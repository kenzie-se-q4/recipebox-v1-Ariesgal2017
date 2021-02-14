"""
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Recipe(models.Model):
    title = models.CharField(max_length=75)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_Required = models.CharField(max_length=30) 
    category = models.CharField(max_length=20)
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




class Author(models.Model):
    name = models.CharField(max_length=150)
    bio = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
         
    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=75)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    time_required = models.DateTimeField(default=timezone.now)
    instructions = models.TextField()
     
    def __str__(self):
        return f"{self.title} | {self.author}"