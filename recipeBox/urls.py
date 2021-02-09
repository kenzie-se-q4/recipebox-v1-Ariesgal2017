from django.contrib import admin
from django.urls import path
from homepage.views import index, recipe_detail, author_detail, add_recipe, add_author

urlpatterns = [
    path('', index, name="homepage"),
    path('recipes/<int:post_id>/', recipe_detail, name="recipe_detail"),
    path('authors/<int:author_id>/', author_detail),
    path('recipe/submit/', add_recipe, name="add_recipe"),
    path('author/submit/', add_author, name="add_author"),

    path('admin/', admin.site.urls),
]