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
    messages = []
    items_list = []
    if request.method == 'POST':
        data = request.get_json()
        # print(data)
        items = data['items']
        # print(items)

        for item in items:
            fp_response = requests.get(fairprice_url + '/' + item)
            if fp_response.status_code == 200:
                #item is inside FP DB
                fp_stock = fp_response.json()['data']
                if fp_stock['quantity'] >= 1:
                    message = {"success": True, "message": f"Order placed successfully with fairprice for {item}."}
                    messages.append(message)
                    items_list.append(fp_stock)
                    
            else: # item is not inside FP DB, check CS DB
                cs_response = requests.get(coldstorage_url + '/' + item)
                if cs_response.status_code == 200:
                    cs_stock = cs_response.json()['data']
                    if cs_stock['quantity'] >= 1:
                        message = {"success": True, "message": f"Order placed successfully with Cold Storage for {item}."}
                        messages.append(message)
                        items_list.append(cs_stock)

            if fp_response.status_code == 404 and cs_response.status_code == 404:
                message = {"success": False, "message": f"Order failed. {item} are out of stock."}
                messages.append(message)



        # print(messages)
        # print(items_list)
        return jsonify(messages)
    
    # if request.method == 'GET':
    #     return jsonify(items_list)

 #------------------- JADEN"S code-------------

        # return jsonify(items)
        

    # return jsonify({'result':'success'})








    # messages = []
    # # Check fairprice stock
    # all_items_fairprice = True
    # all_items_coldstorage = True
    # for item in input_json['items']:
    #     response = requests.get(fairprice_url + '/' + item['itemName'])
    #     if response.status_code == 200:
    #         stock = response.json()['data']
    #         if stock['quantity'] >= item['quantity']:
    #             message = {"success": True, "message": f"Order placed successfully with fairprice for {item['itemName']}."}
    #             messages.append(message)
    #         else:
    #             all_items_fairprice = False
    #     else:
    #         all_items_fairprice = False

    # # Check coldstorage stock
    # if not all_items_fairprice:
    #     for item in input_json['items']:
    #         response = requests.get(coldstorage_url + '/' + item['itemName'])
    #         if response.status_code == 200:
    #             stock = response.json()['data']
    #             if stock['quantity'] >= item['quantity']:
    #                 message = {"success": True, "message": f"Order placed successfully with coldstorage for {item['itemName']}."}
    #                 messages.append(message)
    #             else:
    #                 all_items_coldstorage = False
    #         else:
    #             all_items_coldstorage = False

    # # Generate final message
    # if all_items_fairprice:
    #     message = {"success": True, "message": "Order placed successfully with fairprice."}
    #     messages.append(message)
    # elif all_items_coldstorage:
    #     message = {"success": True, "message": "Order placed successfully with coldstorage."}
    #     messages.append(message)
    # else:
    #     message = {"success": False, "message": "Order failed. All requested items are out of stock."}
    #     messages.append(message)

    # return jsonify(messages)


if __name__ == '__main__':
    app.run(port=5002, debug=True)
