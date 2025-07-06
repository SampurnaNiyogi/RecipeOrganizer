#from django.db import models
from mongoengine import SequenceField, StringField, IntField, DateTimeField, EmailField, Document, ReferenceField, FloatField
from datetime import datetime
import mongoengine as me

class Users(Document):
    user_id = SequenceField(primary_key=True)
    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password_hash = StringField(required=True)
    #date_joined = DateTimeField(default=datetime.UTC)

class Recipes(Document):
    recipe_id = SequenceField(primary_key=True)
    title = StringField(required=True)
    description = StringField()
    instructions = StringField()
    image_url = StringField()
    user_id = ReferenceField(Users, required=True)
    #created_at = DateTimeField(default=datetime.UTC)

class Ingredients(Document):
    ingredient_id = SequenceField(primary_key=True)
    name = StringField(required=True, unique=True)

class RecipeIngredient(Document):
    recipe_id = ReferenceField(Recipes, required=True)
    ingredient_id = ReferenceField(Ingredients, required=True)
    quantity = FloatField(required=True)
    unit = StringField(required=True)

class NutritionInfo(Document):
    recipe_id = ReferenceField(Recipes, required=True)
    calories = IntField()
    protein = IntField()
    fat = IntField()
    carbs = IntField()
    fiber = IntField()
    sugar = IntField()
    sodium = IntField()

class Categories(Document):
    category_id = SequenceField(primary_key=True)
    name = StringField(required=True, unique=True)

class RecipeCategories(Document):
    recipe_id = ReferenceField(Recipes, required=True)
    category_id = ReferenceField(Categories, required=True)

