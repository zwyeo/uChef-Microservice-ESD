from flask import Flask, request, jsonify
from flask_cors import CORS
import stripe
import os, sys

import requests

app = Flask(__name__)
CORS(app)

order_URL = "http://localhost:5002/order"
fairprice_URL = "http://localhost:5003/fairPrice"
coldStorage_URL = "http://localhost:5004/coldStorage"
payment_URL = "http://localhost:5005/payment"
notification_url = "http://localhost:5006/notification"
error_url = "http://localhost:5007/error"
recipe = "http://localhost:5008/recipe"
orderStatus = "http://localhost:5009/orderStatus"




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
        print(session)
    
    return {}



if __name__== '__main__':
    app.run(port=5001, debug=True)