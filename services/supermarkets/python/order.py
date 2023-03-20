from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

fairprice_url = "http://localhost:5003/supermarketStock"
coldstorage_url = "http://localhost:5004/supermarketStock"
delivery_url = "http://localhost:5001/delivery"

@app.route('/order', methods=['POST'])
def place_order():
    # Hardcoded JSON object as input for demonstration
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
    messages = []
    # Check fairprice stock
    all_items_fairprice = True
    all_items_coldstorage = True
    for item in input_json['items']:
        response = requests.get(fairprice_url + '/' + item['itemName'])
        if response.status_code == 200:
            stock = response.json()['data']
            if stock['quantity'] >= item['quantity']:
                message = {"success": True, "message": f"Order placed successfully with fairprice for {item['itemName']}."}
                messages.append(message)
            else:
                all_items_fairprice = False
        else:
            all_items_fairprice = False

    # Check coldstorage stock
    if not all_items_fairprice:
        for item in input_json['items']:
            response = requests.get(coldstorage_url + '/' + item['itemName'])
            if response.status_code == 200:
                stock = response.json()['data']
                if stock['quantity'] >= item['quantity']:
                    message = {"success": True, "message": f"Order placed successfully with coldstorage for {item['itemName']}."}
                    messages.append(message)
                else:
                    all_items_coldstorage = False
            else:
                all_items_coldstorage = False

    # Generate final message
    if all_items_fairprice:
        message = {"success": True, "message": "Order placed successfully with fairprice."}
        messages.append(message)
    elif all_items_coldstorage:
        message = {"success": True, "message": "Order placed successfully with coldstorage."}
        messages.append(message)
    else:
        message = {"success": False, "message": "Order failed. All requested items are out of stock."}
        messages.append(message)

    return jsonify(messages)


if __name__ == '__main__':
    app.run(port=5002, debug=True)
