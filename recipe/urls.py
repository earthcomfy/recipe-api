from django.urls import path

from recipe import views

app_name = 'recipe'

urlpatterns = [
    path('', views.RecipeListAPIView.as_view(), name="recipe_list"),
    path('<int:pk>/', views.RecipeAPIView.as_view(), name="recipe_detail"),
    path('create/', views.RecipeCreateAPIView.as_view(), name="recipe_create"),
]
