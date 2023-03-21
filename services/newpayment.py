from flask import Flask, redirect, request, render_template, url_for, jsonify
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

@app.route("/create-checkout-session")
def create_checkout_session():
    domain_url = "http://127.0.0.1:5005/"

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
            cancel_url=domain_url + "cancelled",
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
      "price_data": {
        "currency": "sgd",
        "product_data": {"name": "T-shirt"},
        "unit_amount": 5000,
      },
      "quantity": 3,
    },
            ]
        )
        return jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 403




if __name__== '__main__':
    app.run(port=5005, debug=True)