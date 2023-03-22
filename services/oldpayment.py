from flask import Flask, redirect, request, render_template, url_for, jsonify

import stripe
import os


app = Flask(__name__)


stripe.api_key = 'sk_test_51MmDHTHHejWNjfqnvGdRbaOCNtclUwprKx9MZXPvtEuRwPnaXtQdXt9ROhbZ1yMhkUJHPhBjOwRLSoEW8ULlfsZM00TtyTrit9'


@app.route('/')
def checkout():
   return render_template('checkout.html')

@app.route('/success')
def thanks():
   return render_template('success.html')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
  input_json = {
        "items": [
            {
                "itemName": "Grape",
                "quantity": 5,
                "price": 1.25
            },
            {
                "itemName": "Apple",
                "quantity": 3,
                "price": 0.75
            },
            {
                "itemName": "Pear",
                "quantity": 2,
                "price": 0.5
            }
        ]
    }
  
  
  session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[
    {
      "price_data": {
        "currency": "sgd",
        "product_data": {"name": "T-shirt"},
        "unit_amount": 5000,
      },
      "quantity": 3,
    },
  ],
    mode='payment',
    success_url= 'http://localhost:5005/success',
    cancel_url='http://localhost:5005/cancel',
  )

  return redirect(session.url, code=303)



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
    print('HELLO')
    return {}

if __name__== '__main__':
    app.run(port=5010, debug=True)
