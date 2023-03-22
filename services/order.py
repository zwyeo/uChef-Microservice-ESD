from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

fairprice_url = "http://localhost:5003/supermarketStock"
coldstorage_url = "http://localhost:5004/supermarketStock"
delivery_url = "http://localhost:5001/delivery"

@app.route('/order', methods=['GET','POST'])
def place_order():
    # Hardcoded JSON object as input for demonstration
    # this code never account for items that are not in both DB 
    # input_json = {
    #     "items": [
    #         {
    #             "itemName": "Grape",
    #             "quantity": 5,
    #             "price": 1.25
    #         },
    #         {
    #             "itemName": "Apple",
    #             "quantity": 3,
    #             "price": 0.75
    #         },
    #         {
    #             "itemName": "Pear",
    #             "quantity": 2,
    #             "price": 0.5
    #         }
    #     ]
    # }
    items_list = []
    total_price = 0
    supermarket = ""
    success = True

    if request.method == 'POST':
        data = request.get_json()
        items = data['items']

        for item in items:
            print(item)
            fp_response = requests.get(fairprice_url + '/' + str(item))
            if fp_response.status_code == 200:
                #item is inside FP DB
                fp_stock = fp_response.json()['data']
                if fp_stock['quantity'] >= 1:
                    items_list.append({"item": item, "price": fp_stock['price'], "quantity": 1})
                    total_price += fp_stock['price']
                    supermarket = "Fairprice"
                else:
                    success = False
                    break # Stop the loop if the item is not available
            else: # item is not inside FP DB, check CS DB
                cs_response = requests.get(coldstorage_url + '/' + str(item))
                if cs_response.status_code == 200:
                    cs_stock = cs_response.json()['data']
                    if cs_stock['quantity'] >= 1:
                        items_list.append({"item": item, "price": cs_stock['price'], "quantity": 1})
                        total_price += cs_stock['price']
                        supermarket = "Cold Storage"
                    else:
                        success = False
                        break # Stop the loop if the item is not available
                else:
                    success = False
                    break # Stop the loop if the item is not available

        response = {
            "success": success,
            "supermarket":supermarket if success else None,
            "totalprice": total_price if success else None,
            "order": items_list if success else None
        }
        return jsonify(response)
    

if __name__ == '__main__':
    app.run(port=5002, debug=True)
