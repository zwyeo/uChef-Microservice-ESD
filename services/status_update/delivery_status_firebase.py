# FILE DOES NOT FUCKING WORK NEEDS MORE DEBUGGING

import firebase_admin
from firebase_admin import credentials, db

# replace this path with the actual path for serviceAccountKey.json
# right click serviceAccountKey.json in VSCode and click on copy path, then paste it into the path below
# e.g. cred = credentials.Certificate("/Users/douglastoh99/Documents/GitHub/uChef-Microservice-ESD/services/notification/serviceAccountKey.json")
cred = credentials.Certificate("/Users/douglastoh99/Documents/GitHub/uChef-Microservice-ESD/services/status_update/serviceAccountKey.json")

root = db.reference()

def updateDatabase(order_dict):
    print("# sending to firebase" + order_dict)

    # check if orderID exists
    orderID = order_dict['orderID']
    order_ref = root.child('orders').child(orderID)
    if orderID.get() is not None:
        # Update existing user
        order_ref.update(order_dict)
        print(f"User {orderID} updated successfully.")
    else:
        # Create new user
        order_ref.set(order_dict)
        print(f"User {orderID} created successfully.")