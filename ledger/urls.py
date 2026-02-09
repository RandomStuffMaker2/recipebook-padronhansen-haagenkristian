from django.urls import path
from . import views

urlpatterns = [
    path("", views.recipes_list, name="base"),
    path('recipes/list', views.recipes_list, name="recipes_list"),
    path('recipe/1', views.recipe_1, name="recipe/1"),
    path('recipe/2', views.recipe_2, name="recipe/2")
]

app_name = "ledger"