from flask import Flask, request, jsonify
from flask_cors import CORS
import stripe
import os, sys

import requests
# from invokes import invoke_http

app = Flask(__name__)
CORS(app)

order_URL = "http://localhost:5002/order"
fairprice_URL = "http://localhost:5003/supermarketStock"
coldStorage_URL = "http://localhost:5004/supermarketStock"
payment_URL = "http://localhost:5005/payment"
notification_URL = "http://localhost:5006/notification"
error_URL = "http://localhost:5007/error"
recipe_URL = "http://localhost:5008/recipe"
orderStatus_URL = "http://localhost:5009/orderStatus"

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




@app.route('/stripe_webhook', methods=['POST'])
def stripe_webhook():
    print('WEBHOOK called')

    payload = request.data
    sig_header = request.headers['STRIPE_SIGNATURE']
    endpoint_secret = 'whsec_4f0cc54f25624e4d83038964f7e3a97bb0975878bdfcab0c9ca14d4cf75bbc03'
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        print('INVALID')
        return {}, 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print('INVALID SIGNATURE')
        return {}, 400

    # Handle the event
    if event['type'] == 'checkout.session.completed':

        session = event['data']['object']
        email = session['customer_details']['email']
        
        #  2. Invoke the notification microservice
        print('\n-----Invoking notification microservice-----')
        notification_call = requests.post(notification_URL, json=email)
        notification_result = notification_call.json()
        print('notification_result:', notification_result['success'])
        
        print(email)
        # return jsonify(order_result)
  
    return {}


if __name__ == '__main__':
    app.run(port=5001, debug=True)
