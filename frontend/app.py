import streamlit as st
import requests
import pandas as pd

API_BASE = "http://localhost:8000"

st.set_page_config(page_title="Recipe Manager", layout="centered")

# --- Helper Functions ---

def fetch_recipes():
    try:
        resp = requests.get(f"{API_BASE}/recipe/")
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        st.error(f"Error fetching recipes: {e}")
        return []

def fetch_ingredients():
    try:
        resp = requests.get(f"{API_BASE}/ingredient/")
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        st.error(f"Error fetching ingredients: {e}")
        return []

def fetch_links():
    try:
        resp = requests.get(f"{API_BASE}/recipe_ingredient/")
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        st.error(f"Error fetching links: {e}")
        return []

# --- Add a New Recipe ---

st.title("Add a New Recipe")
with st.form("add_recipe_form"):
    title = st.text_input("Recipe Title")
    description = st.text_input("Description (Cuisine)")
    instructions = st.text_area("Instructions")
    image_url = st.text_input("Image URL")
    user_id = st.number_input("User ID", min_value=1, step=1)
    submit_recipe = st.form_submit_button("Submit Recipe")

    if submit_recipe:
        data = {
            "title": title,
            "description": description,
            "instructions": instructions,
            "image_url": image_url,
            "user_id": int(user_id)
        }
        resp = requests.post(f"{API_BASE}/recipe/", json=data, headers={"Content-Type": "application/json"})
        if resp.status_code == 201:
            st.success("Recipe added successfully!")
            st.json(resp.json())
            st.rerun()
        else:
            st.error(f"Failed to add recipe: {resp.text}")

# --- Add a New Ingredient ---

st.title("Add Ingredients")
with st.form("add_ingredient_form"):
    i_name = st.text_input("Ingredient Name")
    submit_ingredient = st.form_submit_button("Add Ingredient")
    if submit_ingredient:
        data = {"name": i_name}
        resp = requests.post(f"{API_BASE}/ingredient/", json=data, headers={"Content-Type": "application/json"})
        if resp.status_code == 201:
            st.success("Ingredient added successfully!")
            st.json(resp.json())
            st.rerun()
        else:
            st.error(f"Failed to add ingredient: {resp.text}")

# --- Display Recipes and Ingredients ---

st.header("Recipes and Ingredients List")

recipes = fetch_recipes()
ingredients = fetch_ingredients()

if recipes:
    recipes_df = pd.DataFrame(recipes)
    st.subheader("Recipes")
    st.dataframe(recipes_df)
else:
    st.info("No recipes found.")

if ingredients:
    ingredients_df = pd.DataFrame(ingredients)
    st.subheader("Ingredients")
    st.dataframe(ingredients_df)
else:
    st.info("No ingredients found.")

# --- Link Ingredients to Recipes ---

st.title("Recipe Ingredient")

recipes = fetch_recipes()
ingredients = fetch_ingredients()

recipe_options = {f"{r['title']} (ID: {r['recipe_id']})": r['recipe_id'] for r in recipes}
ingredient_options = {f"{i['name']} (ID: {i['ingredient_id']})": i['ingredient_id'] for i in ingredients}

st.header("Link an Ingredient to a Recipe")
with st.form("link_form"):
    recipe_choice = st.selectbox("Select Recipe", options=list(recipe_options.keys()))
    ingredient_choice = st.selectbox("Select Ingredient", options=list(ingredient_options.keys()))
    quantity = st.number_input("Quantity", min_value=0.0, step=0.1)
    unit = st.text_input("Unit (e.g., grams, cups)")
    submit_link = st.form_submit_button("Link Ingredient")

    if submit_link:
        payload = {
            "recipe_id": recipe_options[recipe_choice],
            "ingredient_id": ingredient_options[ingredient_choice],
            "quantity": quantity,
            "unit": unit
        }
        resp = requests.post(f"{API_BASE}/recipe_ingredient/", json=payload)
        if resp.status_code in (200, 201):
            st.success("Ingredient linked to recipe successfully!")
            st.rerun()
        else:
            st.error(f"Failed to link: {resp.text}")

# --- Display Existing Recipe-Ingredient Links ---

st.header("Existing Recipe-Ingredient Links")
links = fetch_links()
if links:
    links_df = pd.DataFrame(links)
    st.dataframe(links_df)
else:
    st.info("No links found.")
