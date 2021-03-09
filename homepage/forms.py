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
#!added fields to your add recipe form that were missing.
class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=75)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=100)


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            "name",
            "bio",
        ]

class SignupForm(forms.Form):
    name = forms.CharField(max_length=150)
    bio = forms.CharField(max_length=100)
    username = forms.CharField(max_length=36)
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=36)
    password = forms.CharField(widget=forms.PasswordInput)

##ADDED BY BRITT BANNISTER:
class EditRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'author',
            'time_required',
            'instructions',
            'description'
        ]