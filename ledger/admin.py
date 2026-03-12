from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredientQuantity, Profile, RecipeImage
# Register your models here.

class RecipeIngredientQuantityInline(admin.TabularInline):
    model = RecipeIngredientQuantity

class RecipeImageInLine(admin.TabularInline):
    model = RecipeImage

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientQuantityInline, RecipeImageInLine]

admin.site.register(Profile)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredientQuantity)
admin.site.register(RecipeImage)

