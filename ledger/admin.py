from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredientQuantity, Profile
# Register your models here.

class RecipeIngredientQuantityInline(admin.TabularInline):
    model = RecipeIngredientQuantity

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientQuantityInline]

admin.site.register(Profile)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredientQuantity)

