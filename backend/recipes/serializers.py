from rest_framework_mongoengine import serializers
from .models import Recipes, Ingredients, RecipeIngredients, NutritionInfo, Categories, RecipeCategories

class RecipesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Recipes
        fields = '__all__'

class IngredientSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'

class RecipeIngredientSerializer(serializers.DocumentSerializer):
    class Meta:
        model = RecipeIngredients
        fields = '__all__'

class NutritionInfoSerializer(serializers.DocumentSerializer):
    class Meta:
        model = NutritionInfo
        fields = '__all__'

class CategoriesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class RecipeCategoriesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = RecipeCategories
        fields = '__all__'

