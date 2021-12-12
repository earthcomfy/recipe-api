from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Recipe, RecipeCategory


class RecipeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeCategory
        fields = ('id', 'name')


class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'category', 'picture', 'title', 'desc',
                  'cook_time', 'ingredients', 'procedure', 'author')
