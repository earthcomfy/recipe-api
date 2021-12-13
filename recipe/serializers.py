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
    category = RecipeCategorySerializer()

    class Meta:
        model = Recipe
        fields = ('id', 'category', 'category_name', 'picture', 'title', 'desc',
                  'cook_time', 'ingredients', 'procedure', 'author', 'username')

    def get_username(self, obj):
        return obj.author.username

    def get_category_name(self, obj):
        return obj.category.name

    def create(self, validated_data):
        category = validated_data.pop('category')
        category_instance, created = RecipeCategory.objects.get_or_create(
            **category)
        recipe_instance = Recipe.objects.create(
            **validated_data, category=category_instance)
        return recipe_instance

    def update(self, instance, validated_data):
        if 'category' in validated_data:
            nested_serializer = self.fields['category']
            nested_instance = instance.category
            nested_data = validated_data.pop('category')

            nested_serializer.update(nested_instance, nested_data)

        return super(RecipeSerializer, self).update(instance, validated_data)
