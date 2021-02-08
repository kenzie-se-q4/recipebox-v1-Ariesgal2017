from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.models import Author, Recipe
from homepage.forms import RecipeForm, AuthorForm
# Create your views here.


def index(request):
    recipes = Recipe.objects.all()
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
    recipes = Recipe.objects.filter(author=author_obj)
    return render(
        request,       
        "author_detail.html", {
            "author": author_obj,
            "recipes": recipes,
    }
)

def recipe_submit(request):
    context = {}
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data()
            new_item = RecipeForm.objects.create(
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
        "recipe_form.html", 
        context
    )

def author_submit(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = AuthorForm()
    return render(request, "author_form.html", {"form": form})