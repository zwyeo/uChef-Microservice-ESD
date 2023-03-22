from flask import Flask, request, jsonify
from flask_cors import CORS
# import stripe
import os, sys

import requests
# from invokes import invoke_http

app = Flask(__name__)
CORS(app)

order_URL = "http://localhost:5002/order"
fairprice_URL = "http://localhost:5003/supermarketStock"
coldStorage_URL = "http://localhost:5004/supermarketStock"
payment_URL = "http://localhost:5005/payment"
notification_url = "http://localhost:5006/notification"
error_url = "http://localhost:5007/error"
recipe = "http://localhost:5008/recipe"
orderStatus = "http://localhost:5009/orderStatus"

@app.route('/delivery', methods=['POST'])
def place_delivery():
    # data = request.get_json()
    in_data = {
   "items":[
      "Beef",
      "Vegetable Oil",
      "Cinnamon Stick",
      "Cloves",
      "Star Anise",
      "Cardamom",
      "Coconut Cream",
      "Water",
      "Tamarind Paste",
      "Lime",
      "Sugar",
      "Challots"
   ]
}

    
    # 1. Invoke the order microservice
    print('\n-----Invoking order microservice-----')
    order_call = requests.post(order_URL, json=in_data)
    order_result = order_call.json()
    print('order_result:', order_result['success'])


    return jsonify(order_result)






if __name__ == '__main__':
    app.run(port=5001, debug=True)
