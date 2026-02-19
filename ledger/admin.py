from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredientQuantity
# Register your models here.

class RecipeIngredientQuantityInline(admin.TabularInline):
    model = RecipeIngredientQuantity

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientQuantityInline]

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredientQuantity)

