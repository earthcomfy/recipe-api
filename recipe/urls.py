from django.urls import path

from recipe import views

app_name = 'recipe'

urlpatterns = [
    path('', views.RecipeList.as_view(), name="recipe_list"),
    path('<int:pk>/', views.RecipeDetail.as_view(), name="recipe_detail"),
    path('create/', views.RecipeCreate.as_view(), name="recipe_create"),
    path('<int:pk>/update/', views.RecipeUpdate.as_view(), name="recipe_update"),
    path('<int:pk>/delete/', views.RecipeDestroy.as_view(), name="recipe_destroy"),
]
