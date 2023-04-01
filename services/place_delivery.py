from flask import Flask, request, jsonify
from flask_cors import CORS
import stripe
import requests
import amqp_setup
import pika

app = Flask(__name__)
CORS(app)

stripe.api_key = 'sk_test_51MmDHTHHejWNjfqnvGdRbaOCNtclUwprKx9MZXPvtEuRwPnaXtQdXt9ROhbZ1yMhkUJHPhBjOwRLSoEW8ULlfsZM00TtyTrit9'

order_URL = "http://host.docker.internal:5002/order"
fairprice_URL = "http://host.docker.internal:5003/supermarketStock"
coldStorage_URL = "http://host.docker.internal:5004/supermarketStock"
payment_URL = "http://host.docker.internal:5005/create-checkout-session"
notification_URL = "http://host.docker.internal:5006/notification"
error_URL = "http://host.docker.internal:5007/error"
recipe_URL = "http://host.docker.internal:5008/recipes"
supermarketForm_URL = "http://host.docker.internal:5100/"


# First process in getting the initial delivery order 
@app.route('/delivery', methods=['POST'])
def place_delivery():
    data = request.get_json()
  
    # 1. Invoke the order microservice
    print('\n-----Invoking order microservice-----')
    print("data is: ", data)
    order_call = requests.post(order_URL, json=data)
    print("order call is: ", order_call)
    order_result = order_call.json()

    if order_result['success'] == False:
        #2. Invoke recipe microservice
        print('\n-----Invoking recipe microservice-----')
        details = {
                   'category':data['category'], 
                   'id':data['id'] 
                   }
        recipe_call = requests.get(recipe_URL, json=details)
        recipe_result = recipe_call.json()


        # 3. Invoke error microservice since there is error
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='order.error', body="Error: The items in the delivery order are out of stock", properties=pika.BasicProperties(delivery_mode = 2))
        print(recipe_result)

        # Return similar recipes to recommend the customer
        return jsonify(recipe_result)
    
    print('order_result:', order_result['success'])

    return jsonify(order_result)


# Second process of front end requesting for stripe session ID 
@app.route('/get_sessionid', methods=['POST'])
def get_sessionid():
        data = request.get_json()
        # 1. Invoke the payment microservice
        print('\n-----Invoking payment microservice-----')

        # Retrieve Session ID
        payment_call = requests.post(payment_URL, json=data)
        payment_result = payment_call.json()
        return jsonify(payment_result)

# Stripe sends post message to signal that payment has been made and sends payment details
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

        # Get checkout session payment details of customer
        session = stripe.checkout.Session.list(limit=1)
        email = session['data'][0]['customer_details']['email']
        address = session['data'][0]['custom_fields'][0]['text']['value']
        postal_code = session['data'][0]['custom_fields'][1]['text']['value']
        amount = session['data'][0]['amount_total']
        price = "$" + str("{:.2f}".format(amount/100))
        
        print(session['data'])
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
    app.run(host='0.0.0.0', port=5001, debug=True)
