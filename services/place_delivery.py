from flask import Flask, request, jsonify
from flask_cors import CORS
import stripe
import requests
import amqp_setup
import pika

app = Flask(__name__)
CORS(app)

stripe.api_key = 'sk_test_51MmDHTHHejWNjfqnvGdRbaOCNtclUwprKx9MZXPvtEuRwPnaXtQdXt9ROhbZ1yMhkUJHPhBjOwRLSoEW8ULlfsZM00TtyTrit9'

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

    if order_result['success']:
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='order.error', body="error", properties=pika.BasicProperties(delivery_mode = 2))

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

        # checkout_session = event['data']
        # email = checkout_session['object']['customer_details']['email']
        session = stripe.checkout.Session.list(limit=1)
        email = session['data'][0]['customer_details']['email']
        address = session['data'][0]['custom_fields'][0]['text']['value']
        postal_code = session['data'][0]['custom_fields'][1]['text']['value']
        amount = session['data'][0]['amount_total']
        price = "$" + str("{:.2f}".format(amount/100))
        # print(session['data'][0]['amount_total'])
        # print(email)
        data = {
            'price': price,
            'email': email,
            'street_address': address,
            'postal_code': postal_code,
        }

        #  2. Invoke the notification microservice
        print('\n-----Invoking notification microservice-----')
        notification_call = requests.post(notification_URL, json=data)
        print(notification_call.json())
        return {}
  
    return {}


if __name__ == '__main__':
    app.run(port=5001, debug=True)