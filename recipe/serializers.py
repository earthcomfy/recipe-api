from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Recipe, RecipeCategory


class RecipeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeCategory
        fields = ('id', 'name')


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
