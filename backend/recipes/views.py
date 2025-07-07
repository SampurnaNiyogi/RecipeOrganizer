from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Recipes, Ingredients, RecipeIngredients, NutritionInfo, Categories, RecipeCategories
from .serializers import RecipesSerializer, IngredientSerializer, RecipeIngredientSerializer, NutritionInfoSerializer, CategoriesSerializer, RecipeCategoriesSerializer
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