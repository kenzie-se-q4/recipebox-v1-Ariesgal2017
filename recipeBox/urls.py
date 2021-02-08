from django.contrib import admin
from django.urls import path
from homepage.views import index, recipe_detail, author_detail, recipe_submit, author_submit

urlpatterns = [
    path('', index, name="homepage"),
    path('recipes/<int:post_id>/', recipe_detail, name="recipe_detail"),
    path('authors/<int:author_id>/', author_detail),
    path('recipe/submit/', recipe_submit, name="recipe_submit"),
    path('author/submit/', author_submit, name="author_submit"),

    path('admin/', admin.site.urls),
]