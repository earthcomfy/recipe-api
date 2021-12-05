from django.contrib import admin
from .models import RecipeCategory, Recipe

# Register your models here.
admin.site.register(RecipeCategory)
admin.site.register(Recipe)
