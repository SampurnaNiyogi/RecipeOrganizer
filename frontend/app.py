import streamlit as st
import requests

st.title("Add a New Recipe")

title = st.text_input("Recipe Title")
description = st.text_input("Description (Cuisine)")
instructions = st.text_area("Instructions")
image_url = st.text_input("Image URL")
user_id = st.number_input("User ID", min_value=1, step=1)

if st.button("Submit Recipe"):
    data = {
        "title": title,
        "description": description,
        "instructions": instructions,
        "image_url": image_url,
        "user_id": int(user_id)
    }
    response = requests.post(
        "http://localhost:8000/add_recipe/",
        json=data,
        headers={"Content-Type": "application/json"}
    )
    if response.status_code == 201:
        st.success("Recipe added successfully!")
        st.json(response.json())
    else:
        st.error(f"Failed to add recipe: {response.text}")
