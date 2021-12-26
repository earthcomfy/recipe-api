from django.test import TestCase
from django.contrib.auth import get_user_model

from .factories import RecipeCategoryFactory, RecipeFactory, RecipeLikeFactory
from users.tests.factories import UserFactory


User = get_user_model()


class RecipeCategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = RecipeCategoryFactory()

    def test_string_representation(self):
        category = self.category
        expected_string = category.name
        self.assertEqual(str(category), expected_string)


class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = UserFactory()
        cls.category = RecipeCategoryFactory()
        cls.recipe = RecipeFactory(author=cls.author, category=cls.category)

    def test_string_representation(self):
        recipe = self.recipe
        expected_string = recipe.title
        self.assertEqual(str(recipe), expected_string)

    def test_get_total_number_of_likes(self):
        recipe = self.recipe
        total_number_of_likes = recipe.recipelike_set.count()
        self.assertEqual(recipe.get_total_number_of_likes(),
                         total_number_of_likes)


class RecipeLikeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.recipe = RecipeFactory()
        cls.recipe_like = RecipeLikeFactory(user=cls.user, recipe=cls.recipe)

    def test_string_representation(self):
        recipe_like = self.recipe_like
        expected_string = recipe_like.user.username
        self.assertEqual(str(recipe_like), expected_string)
