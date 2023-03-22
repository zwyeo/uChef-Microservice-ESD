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
notification_url = "http://localhost:5006/notification"
error_url = "http://localhost:5007/error"
recipe = "http://localhost:5008/recipe"
orderStatus = "http://localhost:5009/orderStatus"

@app.route('/delivery', methods=['POST'])
def place_delivery():
    # data = request.get_json()
    in_data = {
	"items": [{
			"itemName": "Apple",
			"quantity": 5,
			"price": 1.25
		},
		{
			"itemName": "Kiwi",
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
    # print(type(data))
    # print(data['items'])
    response = requests.post(order_URL, json=in_data)
    order_messages = response.json()
    # print(order_messages)
    delivery_messages = []
    items = in_data["items"]
    print(items)
    for item in items:
        # print(item)
        if any(msg['message'].startswith(f"Order placed successfully with fairprice for {item['itemName']}") for msg in order_messages):
            response = requests.get(fairprice_URL + '/' + item['itemName'])
            if response.status_code == 200:
                stock = response.json()['data']
                delivery_messages.append({"success": True, "message": f"Delivery for {item['itemName']} is successful from fairprice", "quantity": item['quantity'], "price": stock['price'] * item['quantity']})
            else:
                delivery_messages.append({"success": False, "message": f"Delivery for {item['itemName']} failed from fairprice"})

        elif any(msg['message'].startswith(f"Order placed successfully with Cold Storage for {item['itemName']}") for msg in order_messages):
            response = requests.get(coldStorage_URL + '/' + item['itemName'])
            if response.status_code == 200:
                stock = response.json()['data']
                delivery_messages.append({"success": True, "message": f"Delivery for {item['itemName']} is successful from cold storage", "quantity": item['quantity'], "price": stock['price'] * item['quantity']})
            else:
                delivery_messages.append({"success": False, "message": f"Delivery for {item['itemName']} failed from cold storage"})

        else:
            delivery_messages.append({"success": False, "message": f"Delivery for {item['itemName']} failed"})

    return jsonify(delivery_messages)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
