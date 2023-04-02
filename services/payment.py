from flask import Flask,request,jsonify
from flask_cors import CORS
import stripe


app = Flask(__name__)
CORS(app)

stripe.api_key = 'sk_test_51MmDHTHHejWNjfqnvGdRbaOCNtclUwprKx9MZXPvtEuRwPnaXtQdXt9ROhbZ1yMhkUJHPhBjOwRLSoEW8ULlfsZM00TtyTrit9'


# create stripe checkout session and returns stripe checkout session id
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
                success_url=domain_url + "my-delivery",
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


if __name__== '__main__':
    app.run(host="0.0.0.0", port=5005, debug=True)
