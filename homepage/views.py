from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.models import Author, Recipe
from homepage.forms import AddRecipeForm, AddAuthorForm, SignupForm, LoginForm
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def index(request):
    recipes = Recipe.objects.all()
    return render(request, "index.html", {
        "heading": "Recipe",
        "recipes": recipes
    }
)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid:
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(
                    request, username=data['username'], password=data['password']
                )
                if user:
                    login(request, user)
                    return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
            return HttpResponseRedirect(reverse("homepage"))

    form = LoginForm()
    return render(request, "generic_form.html", {'form': form})

"""
localhost:8000/recipe/3

"""
def recipe_detail(request, post_id):
    recipe = Recipe.objects.get(id=post_id)
    return render(
        request,
        "recipe_detail.html", {
            "recipe": recipe,
    }
)

def author_detail(request, author_id):
    author_obj = Author.objects.get(id=author_id)
    recipes = Recipe.objects.filter(author=author_obj)
    return render(
        request,       
        "author_detail.html", {
            "author": author_obj,
            "recipes": recipes,
    }
)

@login_required
def addRecipe(request):
    context = {}
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_item = Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                body=data['body'],
                description=data['description'],
            )
            return HttpResponseRedirect(reverse("recipe_detail", args=[new_item.id]))
    form=RecipeForm()
    context.update({'message': "Submitted Successfully!!!!! YAY!"})
    form = RecipeForm()
    context.update({'form': form})
    return render(
        request, 
        "addRecipe.html", 
        context
    )

@login_required
def addAuthor(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = AuthorForm()
    return render(request, "addAuthor.html", {"form": form})

def login(request):
    if request.method == 'POST':
        form = Login_user(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid:
            if form.is_valid():
                data = form.cleaned_data
                new_user = User.objects.create(
                username=data['username'], password=data['password']
            )
            Author.objects.create(
                name=data['name'],
                bio=data['bio'],
                user=new_user
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = SignupForm()
    return render(request, "generic_form.html", {'form': form})