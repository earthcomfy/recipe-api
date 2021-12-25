from django.test import TestCase
from django.contrib.auth import get_user_model

from .factories import RecipeCategoryFactory, RecipeFactory
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
