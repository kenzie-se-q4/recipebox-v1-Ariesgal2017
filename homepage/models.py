<<<<<<< Updated upstream
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
=======
from django.db import models
from django.shortcuts import render
from recipeBox import settings
"""
Author model:

*   Name (CharField)
*   Bio (TextField)

Recipe Model:

*   Title (CharField)
*   Author (ForeignKey)
*   Description (TextField)
*   Time Required (Charfield) (for example, "One hour")
*   Instructions (TextField)

"""
# Create your models here.

class Author(models.Model):
    pass

class Ticket(models.Model):
    title = models.CharField(max_length=20)
    # timeDateFiled = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=50)
    userWhoFiledTicket = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = '+', on_delete=models.CASCADE)
    ticketStatus = models.CharField(max_length=2)
    possibleStatuses = (('N', 'New'),
                        ('IP', 'In Progress'),
                        ('D', 'Done'),
                        ('IV', 'Invalid'),
    )
    userAssignedToTicket = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='+', on_delete=models.CASCADE)
    userWhoCompletedTicket = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='+', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
>>>>>>> Stashed changes
