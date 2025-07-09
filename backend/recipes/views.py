from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Recipes, Ingredients, RecipeIngredients, NutritionInfo, Categories, RecipeCategories
from .serializers import RecipesSerializer, IngredientSerializer, RecipeIngredientSerializer, NutritionInfoSerializer, CategoriesSerializer, RecipeCategoriesSerializer
from bson import ObjectId
# Create your views here.
def index(request):
    return HttpResponse("Hi Django!!")


#Add/List recipes
class ListCreateRecipe(generics.ListCreateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer

#Update/List/Delete recipes    
class RetrieveUpdateDestroyRecipe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
    
class ListCreateIngredient(generics.ListCreateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer

class RetriveUpdateDestroyIngredient(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer
    
class ListCreateRecipeIngredient(generics.ListCreateAPIView):
    queryset = RecipeIngredients.objects.all()
    serializer_class = RecipeIngredientSerializer

class ListCreateNutritionInfo(generics.ListCreateAPIView):
    queryset = NutritionInfo.objects.all()
    serializer_class = NutritionInfoSerializer

class RetrieveUpdtateDestroyNutritionInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = NutritionInfo.objects.all()
    serializer_class = NutritionInfoSerializer

class ListCreateCategory(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class RetrieveUpdtateDestroyCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class ListCreateRecipeCategory(generics.ListCreateAPIView):
    queryset = RecipeCategories.objects.all()
    serializer_class = RecipeCategoriesSerializer



#search by filter

#List Recipes by Category
class RecipesByCategory(generics.ListAPIView):
    serializer_class = RecipesSerializer

    def get_queryset(self):
        category_id = int(self.kwargs.get('category_id'))
        # Get all recipe IDs linked to this category
        recipe_ids = [
        rc.recipe_id for rc in RecipeCategories.objects.filter(category_id=category_id)
        ]
        return Recipes.objects.filter(recipe_id__in=[r.recipe_id for r in recipe_ids])



#List Recipes by Ingredient
class RecipeByIngredient(generics.ListAPIView):
    serializer_class = RecipesSerializer

    def get_queryset(self):
        ingredient_id = int(self.kwargs.get('ingredient_id'))

        recipe_ids = [ 
            ri.recipe_id for ri in RecipeIngredients.objects.filter(ingredient_id=ingredient_id)
        ]
        return Recipes.objects.filter(recipe_id__in=[r.recipe_id for r in recipe_ids])

#List Ingredients by Recipe