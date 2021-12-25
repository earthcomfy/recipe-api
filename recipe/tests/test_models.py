from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from recipe.models import RecipeCategory, Recipe

User = get_user_model()


class RecipeCategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        RecipeCategory.objects.create(name="Appetizer")

    def test_string_representation(self):
        category = RecipeCategory.objects.get(id=1)
        expected_string = category.name
        self.assertEqual(str(category), expected_string)


class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            username='testuser', email='kk@kk.com', password='12three')
        category = RecipeCategory.objects.create(name="Appetizer")
        Recipe.objects.create(
            author=user,
            category=category,
            picture=SimpleUploadedFile(
                name='test_image.jpg',
                content=b'',
                content_type='image/jpeg'),
            title="just another cooking recipe",
            desc="Chocolate dipped dessert is so good",
            cook_time="1:10:10",
            ingredients="milk, coccunut, cream",
            procedure="1. do this, 2. do that, 3. then eat",
        )

    def test_string_representation(self):
        recipe = Recipe.objects.get(id=1)
        expected_string = recipe.title
        self.assertEqual(str(recipe), expected_string)
