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




#! added favorites.
class Author(models.Model):
    name = models.CharField(max_length=150)
    bio = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField('Recipe', symmetrical = False, blank=True, related_name='author_faves')

         
    def __str__(self):
        return self.name

#! changed time_required to a CharField and added missing description field.
class Recipe(models.Model):
    title = models.CharField(max_length=75)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    time_required = models.CharField(max_length=50)
    description = models.TextField()
    instructions = models.TextField()
     
    def __str__(self):
        return f"{self.title} | {self.author}"