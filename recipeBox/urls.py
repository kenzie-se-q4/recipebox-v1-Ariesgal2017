from django.contrib import admin
from django.urls import path
from homepage.views import index, recipe_detail, author_detail, signup_view, login_view
from homepage.views import index, recipe_detail, author_detail, recipe_submit, author_submit

urlpatterns = [
    # path('', index),
    path('recipes/<int:post_id>/', recipe_detail),
    path('', index, name="homepage"),
    path('recipes/<int:post_id>/', recipe_detail, name="recipe_detail"),
    path('authors/<int:author_id>/', author_detail),
    path('AddRecipe/', recipe_submit, name="recipe_submit"),
    path('AddAuthor/', author_submit, name="author_submit"),
    path('login/', login_view, name="login"),
    path('signup/', signup_view, name="signup"),
    path('admin/', admin.site.urls),
]