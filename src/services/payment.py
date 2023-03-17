from flask import Flask, redirect, request, render_template, url_for

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

if __name__== '__main__':
    app.run(port=5005, debug=True)
