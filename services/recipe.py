from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

app = Flask(__name__)

# Initialize Firebase app
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://esd-uchef-restore-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Get a reference to the database
ref = db.reference('popularRecipe')

# Define a route to retrieve data from Firebase
@app.route('/recipes')
def get_recipes():
    data = ref.get()
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5091, debug=True)