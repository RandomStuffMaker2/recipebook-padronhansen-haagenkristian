from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Recipe

# Create your views here.

def recipes_list(request):
    recipes = Recipe.objects.all()

    return render(request, "ledger/recipes_list.html", {"recipes": recipes})
@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    return render(request, "ledger/recipe_detail.html", {"recipe": recipe})

