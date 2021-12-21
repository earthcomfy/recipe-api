from django.contrib import admin
from .models import RecipeCategory, Recipe, RecipeLike

# Register your models here.
admin.site.register(RecipeCategory)
admin.site.register(Recipe)
admin.site.register(RecipeLike)
