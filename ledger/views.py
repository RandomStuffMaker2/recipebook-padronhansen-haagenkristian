from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Recipe, Profile
from .forms import RecipeForm, RecipeImageForm

# Create your views here.

def recipes_list(request):
    recipes = Recipe.objects.all()

    return render(request, "ledger/recipes_list.html", {"recipes": recipes})

@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    return render(request, "ledger/recipe_detail.html", {"recipe": recipe})

@login_required
def recipe_add(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            profile = Profile.objects.get(user=request.user)
            recipe.author = profile
            recipe.save()
            return redirect(recipe.get_absolute_url())
        
    else:
        form = RecipeForm()
    return render(request, "ledger/recipe_add.html", {"form": form})

@login_required
def recipe_add_image(request, pk):
    recipe = Recipe.objects.get(pk=pk)
      
    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()
            return redirect(recipe.get_absolute_url())
    else:
        form = RecipeImageForm()

    return render(request, "ledger/recipe_add_image.html",
                  {"form": form, "recipe": recipe} )
