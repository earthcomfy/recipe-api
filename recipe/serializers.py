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
    username = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ('id', 'category', 'category_name', 'picture', 'title', 'desc',
                  'cook_time', 'ingredients', 'procedure', 'author', 'username')

    def get_username(self, obj):
        return obj.author.username

    def get_category_name(self, obj):
        return obj.category.name
