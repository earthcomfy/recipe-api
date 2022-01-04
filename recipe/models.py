from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class RecipeCategory(models.Model):
    """
    Recipe categories
    """
    name = models.CharField(_('Category name'), max_length=100)

    class Meta:
        verbose_name = _('Recipe Category')
        verbose_name_plural = _('Recipe Categories')

    def __str__(self):
        return self.name


def get_default_recipe_category():
    """
    Returns a default recipe type.
    """
    return RecipeCategory.objects.get_or_create(name='Others')[0]


class Recipe(models.Model):
    """
    Recipe model
    """
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="recipes", on_delete=models.CASCADE)
    category = models.ForeignKey(
        RecipeCategory, related_name="recipe_list", on_delete=models.SET(get_default_recipe_category))
    picture = models.ImageField(upload_to='uploads')
    title = models.CharField(max_length=200)
    desc = models.CharField(_('Short description'), max_length=200)
    cook_time = models.TimeField()
    ingredients = models.TextField()
    procedure = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.title

    def get_total_number_of_likes(self):
        return self.recipelike_set.count()

    def get_total_number_of_bookmarks(self):
        return self.bookmarked_by.count()


class RecipeLike(models.Model):
    """
    Model to like recipes
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
