from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path("", views.index, name = "index"),
    path("recipe/", views.ListCreateRecipe.as_view(), name = "Add/List Recipe"),
    path("recipe/<int:pk>/", views.RetrieveUpdateDestroyRecipe.as_view(), name = "Update/List/Delete Recipe"),
    path("ingredient/", views.ListCreateIngredient.as_view(), name = "Add/List Ingredient"),
    path("ingredient/<int:pk>/", views.RetriveUpdateDestroyIngredient.as_view(), name = "Update/List/Delete Ingredient"),
    path("recipe_ingredient/",views.ListCreateRecipeIngredient.as_view(), name = "Add/List Recipe Ingredient Connection"),
    path("nutrition_info/", views.ListCreateNutritionInfo.as_view(), name = "Add/List Nutrition Info"),
    path("nutrition_info/<int:pk>/",views.RetrieveUpdtateDestroyNutritionInfo.as_view(), name = "Update/Retrive/Destroy NutritionInfo"),
    path("category/", views.ListCreateCategory.as_view(), name = "Add/List NutritionInfo"),
    path("category/<int:pk>/", views.RetrieveUpdtateDestroyCategory.as_view(), name = "Update/List/Delete Category"),
    path("recipe_category/",views.ListCreateRecipeCategory.as_view(), name = "Add/List Recipe Category"),
    path("category/<int:category_id>/recipe/", views.RecipesByCategory.as_view(), name = "Recipes By Category"),
    path("ingredient/<int:ingredient_id>/recipe/", views.RecipeByIngredient.as_view(), name = "Recipes By Ingredient"),
]   