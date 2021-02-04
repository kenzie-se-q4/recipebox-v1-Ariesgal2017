from django.contrib import admin
from django.urls import path
from homepage.views import index, recipe_detail, author_detail

urlpatterns = [
    path('', index),
    path('recipes/<int:post_id>/', recipe_detail),
    path('authors/<int:author_id>/', author_detail),
    path('admin/', admin.site.urls),
]