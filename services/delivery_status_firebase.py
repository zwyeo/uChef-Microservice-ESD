import firebase_admin
import requests
from firebase_admin import db
import json

def updateDatabase(order_dict):
    db_url = "https://esd-uchef-restore-default-rtdb.asia-southeast1.firebasedatabase.app/order/{}.json".format(order_dict['orderID'])

    print("# sending to firebase update for order no. " + order_dict['orderID'])

    status = requests.put(db_url, json=json.dumps(order_dict))
    
    print(f"Order {order_dict['orderID']} updated successfully. Status code: {status.status_code}")