from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Recipe
from .serializers import RecipeSerializer


class RecipeList(generics.ListAPIView):
    """
    Get: a collection of recipes
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (AllowAny,)


class RecipeDetail(generics.RetrieveAPIView):
    """
    Get: a single recipe
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (AllowAny,)


class RecipeCreate(generics.CreateAPIView):
    """
    Create: a recipe
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticated,)


class RecipeUpdate(generics.UpdateAPIView):
    """
    Update: a recipe
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticated,)


class RecipeDestroy(generics.DestroyAPIView):
    """
    Delete: a recipe
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticated,)
