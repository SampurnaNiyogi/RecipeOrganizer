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

    def __str__(self):
        return self.title


class Ingredients(Document):
    ingredient_id = SequenceField(primary_key=True)
    name = StringField(required=True, unique=True)

    def __str__(self):
        return self.name


class RecipeIngredients(Document):
    recipe_id = ReferenceField(Recipes, required=True)
    ingredient_id = ReferenceField(Ingredients, required=True)
    quantity = FloatField(required=True)
    unit = StringField(required=True)

    def __str__(self):
        return self.recipe_id


class NutritionInfo(Document):
    recipe_id = ReferenceField(Recipes, required=True, primary_key=True)
    calories = IntField()
    protein = IntField()
    fat = IntField()
    carbs = IntField()
    fiber = IntField()
    sugar = IntField()
    sodium = IntField()

    def __str__(self):
        return self.recipe_id
    

class Categories(Document):
    category_id = SequenceField(primary_key=True)
    name = StringField(required=True, unique=True)

    def __str__(self):
        return self.name
    

class RecipeCategories(Document):
    recipe_id = ReferenceField(Recipes, required=True)
    category_id = ReferenceField(Categories, required=True)

    def __str__(self):
        return self.recipe_id