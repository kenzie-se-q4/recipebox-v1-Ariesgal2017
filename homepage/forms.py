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

from django import forms
from homepage.models import Author, Recipe

class RecipeForm(forms.Form):
    title = forms.CharField(max_length=75)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    category = forms.CharField(max_length=20)

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            "name",
            "bio",
        ]