<<<<<<< Updated upstream
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from homepage.models import Author, Recipe
from homepage.forms import AddRecipeForm, AddAuthorForm, SignupForm, LoginForm
# Create your views here.
from django.contrib.auth.decorators import login_required

def author_detail(request, author_id):
    author_obj = Author.objects.get(id=author_id)
    recipes = Recipe.objects.filter(author=author_obj)
    return render(request, "author_detail.html", {
        "author": author_obj,
        "recipes": recipes,
    })


def index(request):
    recipes = Recipe.objects.all()
    return render(request, "index.html", {
        "heading": "Recipes",
        "recipes": recipes
    })
def recipe_detail(request, post_id):
    recipe = Recipe.objects.get(id=post_id)
    return render(request, "recipe_detail.html", {
        "recipe": recipe
    })

@login_required
def recipe_submit(request):
    context = {}
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_item = Recipe.objects.create(
                title=data['title'],
                # author=request.user.Author,
                # i=data['instructions'],
            )
            return HttpResponseRedirect(reverse("homepage", args=[new_item.id]))
    form=AddRecipeForm()
    return render(request, "add_ecipe.html", {"form": form})
    context.update({'form': form})
   
@login_required
def author_submit(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        return HttpResponseRedirect(reverse("homepage"))

    form = AddAuthorForm()
    return render(request, "add_author.html", {"form": form})


def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        new_user = User.objects.create_user(
            username=data['username'], password=data['password']
        )
        new_author = Author.objects.create(
            name=data['name'],
            bio=data['bio'],
            user = new_user
        )
        return HttpResponseRedirect(reverse("homepage"))
    form=SignupForm()
    return render(request, "generic_form.html", {"form": form})
            

def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        user = authenticate(
            request, username=data['username'], password=data['password'])
        if user:
            login(request, user)
        return HttpResponseRedirect(reverse("addRecipe"))
  
    form=LoginForm()
    return render(request, "add_recipe.html", {"form": form})
            





=======
from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.models import Author, Ticket
from homepage.forms import AddRecipeForm, AddAuthorForm
# Create your views here.


def index(request):
    recipes = Ticket.objects.all()
    return render(request, "index.html", {
        "heading": "Recipe",
        "recipes": recipes
    }
)


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
    recipes = Ticket.objects.filter(author=author_obj)
    return render(
        request,       
        "author_detail.html", {
            "author": author_obj,
            "recipes": recipes,
    }
)

def add_recipe(request):
    context = {}
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_item = Ticket.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
            )
            return HttpResponseRedirect(reverse("recipe_detail", args=[new_item.id]))
    form=RecipeForm()
    context.update({'message': "Submitted Successfully!!!!! YAY!"})
    form = RecipeForm()
    context.update({'form': form})
    return render(
        request, 
        "add_recipe.html", 
        context
    )

def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = AuthorForm()
    return render(request, "add_author.html", {"form": form})
>>>>>>> Stashed changes
