from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

app = Flask(__name__)

# Initialize Firebase app
cred = credentials.Certificate("themealdb-5744c-firebase-adminsdk-8izv6-23da3eb002.json")
firebase_admin.initialize_app(cred, {
<<<<<<< HEAD
    'databaseURL': 'https://esd-uchef-restore-default-rtdb.asia-southeast1.firebasedatabase.app/'
=======
    'databaseURL': 'https://themealdb-5744c-default-rtdb.asia-southeast1.firebasedatabase.app/'
>>>>>>> 407157c9adffcd7a5af40d6a5cd3ccfcf9682b2c
})

# Get a reference to the database
ref = db.reference('meals')

# Define a route to retrieve data from Firebase
@app.route('/recipes')
def get_recipes():
    data = ref.get()
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5099, debug=True)