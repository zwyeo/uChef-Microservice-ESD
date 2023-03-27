from flask import Flask, request, jsonify, session
from flask_cors import CORS
import stripe
import requests
from flask_session import Session
# from invokes import invoke_http

app = Flask(__name__)
# Configure the app to use sessions
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
CORS(app)

stripe.api_key = 'sk_test_51MmDHTHHejWNjfqnvGdRbaOCNtclUwprKx9MZXPvtEuRwPnaXtQdXt9ROhbZ1yMhkUJHPhBjOwRLSoEW8ULlfsZM00TtyTrit9'
app.secret_key = 'test'

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
    data = request.get_json()
  


    # 1. Invoke the order microservice
    print('\n-----Invoking order microservice-----')
    order_call = requests.post(order_URL, json=data)
    order_result = order_call.json()
    print('order_result:', order_result['success'])
    # print(order_result['totalprice'])
    session['totalprice'] = order_result['totalprice']
    print(session.get('totalprice'))

    
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

        checkout_session = event['data']
        email = checkout_session['object']['customer_details']['email']
        
        #  2. Invoke the notification microservice
        # print('\n-----Invoking notification microservice-----')
        # notification_call = requests.post(notification_URL, json=email)
        # notification_result = notification_call.json()
        # print('notification_result:', notification_result['success'])
        session = stripe.checkout.Session.list(limit=1)
        # amount_total = session['amount_total']
        print(session['data'][0]['amount_total'])
        print(email)
        # return jsonify(order_result)
  
    return {}


if __name__ == '__main__':
    app.run(port=5001, debug=True)
