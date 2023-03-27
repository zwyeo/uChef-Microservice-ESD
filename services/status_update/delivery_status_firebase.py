# FILE DOES NOT FUCKING WORK NEEDS MORE

import firebase_admin
import requests
from firebase_admin import credentials, db
import json

# replace this path with the actual path for serviceAccountKey.json
# right click serviceAccountKey.json in VSCode and click on copy path, then paste it into the path below
# e.g. cred = credentials.Certificate("/Users/douglastoh99/Documents/GitHub/uChef-Microservice-ESD/services/notification/serviceAccountKey.json")
cred = credentials.Certificate("/Users/douglastoh99/Documents/GitHub/uChef-Microservice-ESD/services/status_update/serviceAccountKey.json")

def updateDatabase(order_dict):
    db_url = "https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/order/{}.json".format(order_dict['orderID'])

    print("# sending to firebase update for order no. " + order_dict['orderID'])

    status = requests.put(db_url, json=json.dumps(order_dict))
    
    print(status.text)
    # print(f"Order {order_dict['orderID']} updated successfully.")