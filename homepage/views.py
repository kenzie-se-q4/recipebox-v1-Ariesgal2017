from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.models import User
#added logout
from django.contrib.auth import login, authenticate, logout
from homepage.models import Author, Recipe
from homepage.forms import AddRecipeForm, AddAuthorForm, SignupForm, LoginForm, EditRecipe
from django.contrib.auth.decorators import login_required

#! added in favorites field from model to render
def author_detail(request, author_id):
    author_obj = Author.objects.get(id=author_id)
    recipes = Recipe.objects.filter(author=author_obj)
    favorites = author_obj.favorites.all()
    return render(request, "author_detail.html", {
        "author": author_obj,
        "recipes": recipes,
        'favorites':favorites
    })


def index(request):
    recipes = Recipe.objects.all()
    return render(request, "index.html", {
        "heading": "Recipes",
        "recipes": recipes
    })

#! changed var name to stay consitent with rest of your code.
def recipe_detail(request, post_id):
    recipe_obj = Recipe.objects.get(id=post_id)
    return render(request, "recipe_detail.html", {
        "recipe": recipe_obj
    })

#! added the rest of your fields. you have a generic_form so you dont need the addition forms. also in your return render, i added your ocntext in.
@login_required
def recipe_submit(request):
    context = {}
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe = Recipe.objects.create(
                title = data['title'],
                author = data['author'],
                description = data['description'],
                time_required = data['time_required'],
                instructions = data['instructions']
            )
            context.update({'message': 'Submitted Recipe Successfully!'})
            return HttpResponseRedirect(reverse('recipe_detail', args=[recipe.id]))

    form = AddRecipeForm()
    context.update({'form':form})
    return render(
        request,
        'generic_form.html',
        context
    )

#! forgot to check if form is valid, added that in. also added in create user and newform. Also added in a condition to check is user is staff to submit the form. added error template.
@login_required
def author_submit(request):
        if request.method == "POST":
            form = AddAuthorForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                usr = User.objects.create_user(
                    username = data['name'],
                )
                newform = Author.objects.create(
                    name = data['name'],
                    user = usr
                )
                newform.save()
            return HttpResponseRedirect(reverse("homepage"))

        form = AddAuthorForm()
        if request.user.is_staff == True:   
            return render(request, "generic_form.html", {"form": form})

        return render(request, 'error.html')

#! fixed this view to make it consistent with the other form views, added authenticate.
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(
                username = data['username'],
                password = data['password']
            )
            user = authenticate(
                username = data['username'],
                password = data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
                return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()
    return render(request, 'generic_form.html', {'form':form})
            
#! not rendering correctly, forgot to add the first if statement, and request.GET.get next-fixed.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, 
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next',reverse('homepage')))
    form=LoginForm()
    return render(request, "generic_form.html", {"form": form})

#!added logout:
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


## CODE ADDED BY BRITT BANNISTER 
@login_required 
def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.filter(id = recipe_id).first()
    if request.method == 'POST':
        form = EditRecipe(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe.title = data['title']
            recipe.time_required = data['time_required']
            recipe.instructions = data['instructions']
            recipe.description = data['description']
            recipe.save()

            return HttpResponseRedirect(reverse('recipe_detail', args=[recipe.id]))
    
    else:
        form = EditRecipe({
            'title': recipe.title,
            'time_required': recipe.time_required,
            'instructions': recipe.instructions,
            'description': recipe.description
        })
        return render(request, 'generic_form.html', {'form':form})


@login_required
def favorite(request, id):
    recipe = Recipe.objects.get(id=id)
    request.user.author.favorites.add(recipe)
    request.user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))