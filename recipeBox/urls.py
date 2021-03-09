from django.contrib import admin
from django.urls import path
from homepage.views import index, recipe_detail, author_detail, recipe_submit, author_submit, login_view, signup_view, logout_view

#! Had multiple urls that were the same, added logout and edit fixed and cleaned up.
urlpatterns = [
    path('', index, name="homepage"),
    path('recipes/<int:post_id>/', recipe_detail, name="recipe_detail"),
    path('authors/<int:author_id>/', author_detail),
    path('recipe/addrecipe/', recipe_submit, name="recipe_submit"),
    # path('recipe/edit/<int:recipe_id>', edit_recipe, name='edit_recipe'),
    path('author/addauthor/', author_submit, name="author_submit"),
    path('login/', login_view, name="login"),
    path('signup/', signup_view, name="signup"),
    path('logout/', logout_view, name='logout'),
    path('admin/', admin.site.urls),
]