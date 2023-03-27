from flask import Flask, redirect, request, render_template, url_for, jsonify,session
from flask_cors import CORS
import stripe
import os


app = Flask(__name__)
CORS(app)

stripe.api_key = 'sk_test_51MmDHTHHejWNjfqnvGdRbaOCNtclUwprKx9MZXPvtEuRwPnaXtQdXt9ROhbZ1yMhkUJHPhBjOwRLSoEW8ULlfsZM00TtyTrit9'


@app.route('/')
def checkout():
   return render_template('checkout.html')

@app.route('/success')
def thanks():
   return render_template('success.html')

@app.route("/create-checkout-session", methods=['GET', 'POST'])
def create_checkout_session():
    if request.method == 'POST':
        orders = request.get_json().get('order')
    
        domain_url = "http://localhost:8080/"
        line_items = []
        for order in orders:
            items = {
        "price_data": {
            "currency": "sgd",
            "product_data": {"name": order.get('item')},
            "unit_amount": int(order.get('price') * 100),
        },
        "quantity": 1,
        }
            line_items.append(items)

        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
                cancel_url=domain_url ,
                payment_method_types=["card"],
                mode="payment",
                line_items=line_items,
                custom_fields=[
                        {
                        "key": "address",
                        "label": {"type": "custom", "custom": "Street Address"},
                        "type": "text",
                        },
                        {
                        "key": "postalcode",
                        "label": {"type": "custom", "custom": "Postal Code"},
                        "type": "text",
                        }
                    ],
                
            )
            return jsonify({"sessionId": checkout_session["id"]})
        except Exception as e:
            return jsonify(error=str(e)), 403


# WEBHOOK -> send success status after user has completed payment
# @app.route('/stripe_webhook', methods=['POST'])
# def stripe_webhook():
#     print('WEBHOOK called')

#     payload = request.data
#     sig_header = request.headers['STRIPE_SIGNATURE']
#     endpoint_secret = 'whsec_4f0cc54f25624e4d83038964f7e3a97bb0975878bdfcab0c9ca14d4cf75bbc03'
#     event = None

#     try:
#         event = stripe.Webhook.construct_event(
#             payload, sig_header, endpoint_secret
#         )
#     except ValueError as e:
#         # Invalid payload
#         print('INVALID')
#         return {}, 400
#     except stripe.error.SignatureVerificationError as e:
#         # Invalid signature
#         print('INVALID SIGNATURE')
#         return {}, 400

#     # Handle the event
#     if event['type'] == 'checkout.session.completed':

#         session = event['data']
#         email = session['object']['customer_details']['email']
        
#         #  2. Invoke the notification microservice
#         # print('\n-----Invoking notification microservice-----')
#         # notification_call = requests.post(notification_URL, json=email)
#         # notification_result = notification_call.json()
#         # print('notification_result:', notification_result['success'])
#         print(session)
#         print(email)
        
#         # return jsonify(order_result)
  
#     return {}

if __name__== '__main__':
    app.run(port=5005, debug=True)
