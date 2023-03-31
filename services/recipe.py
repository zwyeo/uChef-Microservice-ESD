from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

app = Flask(__name__)

# Initialize Firebase app
cred = credentials.Certificate("themealdb-5744c-firebase-adminsdk-8izv6-23da3eb002.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://themealdb-5744c-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Get a reference to the database
ref = db.reference('meals')

# Define a route to retrieve data from Firebase
@app.route('/recipes')


def get_recipes():
    category = "Beef"
    new_arr = []
    data = ref.get()
    similar_recipes = filter_by_category(data, category)
    for d in similar_recipes:
        meal_info = {
            'strMeal': d.get('strMeal'),
            'strMealThumb': d.get('strMealThumb'),
            'idMeal': d.get('idMeal')
        }
        new_arr.append(meal_info)
    return new_arr[0:6]



def filter_by_category(arr, category):
    """
    Filters an array of dictionaries based on the 'strCategory' key matching a given category.
    """
    return [d for d in arr if d.get('strCategory') == category]

if __name__ == '__main__':
    app.run(port=5099, debug=True)