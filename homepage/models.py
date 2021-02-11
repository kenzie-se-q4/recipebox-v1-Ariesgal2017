from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User

"""
User:
-------
username ()
password ()
email ()
one to one

Author model:

*   Name (CharField)
*   Bio (TextField)
one to many


Recipe Model:

*   Title (CharField)
*   Author (ForeignKey)
*   Description (TextField)
*   Time Required (Charfield) (for example, "One hour")
*   Instructions (TextField)

"""
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=75)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_Required = models.CharField(max_length=30) 
    instructions = models.TextField()

    def __str__(self):
        return f"{self.title} | {self.author}"