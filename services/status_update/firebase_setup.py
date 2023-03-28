import firebase_admin
from firebase_admin import credentials, messaging, db

cred = credentials.Certificate("serviceAccountKey.json")

def start():
    firebase_admin.initialize_app(cred, {'databaseURL':'https://uchef-9f3e5.firebaseio.com/'})
    root = db.reference()

    print("firebase instance initialised. root: {}".format(root))