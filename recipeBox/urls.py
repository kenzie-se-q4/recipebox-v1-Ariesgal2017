from django.contrib import admin
from django.urls import path
from homepage.views import index, recipe_detail, author_detail, addRecipe, addAuthor, signup_view, login_view

urlpatterns = [
    path('', index, name="homepage"),
    path('recipes/<int:post_id>/', recipe_detail, name="recipe_detail"),
    path('authors/<int:author_id>/', author_detail),
    path('addRecipe', addRecipe, name="add_recipe"),
    path('addAuthor/', addAuthor, name="add_author"),
    path('signup/', signup_view, name="signup"),
    path('login/', login_view, name="login"),
    path('admin/', admin.site.urls),
]