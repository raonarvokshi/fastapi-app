import streamlit as st
import requests
import pandas
from dotenv import load_dotenv
import os

load_dotenv()

Api_base_url = os.getenv("api_base_url")


def get_categories():
    response = requests.get(f"{Api_base_url}/categories")
    return response.json()


def get_recipes(cuisine=None, difficulty=None):
    param = {}
    if cuisine:
        param["cuisine"] = cuisine

    if difficulty:
        param["difficulty"] = difficulty

    response = requests.get(f"{Api_base_url}/recipes", params=param)

    return response.json()


def create_category(category_name):
    responses = requests.post(
        f"{Api_base_url}/categories", json={"name": category_name})
    return responses.json()


def update_category(category_id, category_name):
    response = requests.put(
        f"{Api_base_url}/categories/{category_id}", json={"name": category_name})
    return response.json()


def delete_category(category_id):
    response = requests.delete(f"{Api_base_url}/categories/{category_id}")
    return response.json()


def create_recipes(recipe_name, description, ingredients, instructions, cuisine, difficulty, category_id):
    response = requests.post(f"{Api_base_url}/recipes", json={
        "name": recipe_name,
        "description": description,
        "ingredients": ingredients,
        "instructions": instructions,
        "cuisine": cuisine,
        "difficulty": difficulty,
        "category_id": category_id
    })
    return response.json()


def update_recipe(recipe_id, recipe_name, description, ingredients, instructions, cuisine, difficulty, category_id):
    response = requests.put(f"{Api_base_url}/recipes/{recipe_id}", json={
        "name": recipe_name,
        "description": description,
        "ingredients": ingredients,
        "instructions": instructions,
        "cuisine": cuisine,
        "difficulty": difficulty,
        "category_id": category_id
    })
    return response.json()


def delete_recipe(recipe_id):
    response = requests.delete(f"{Api_base_url}/recipes/{recipe_id}")
    return response.json()
