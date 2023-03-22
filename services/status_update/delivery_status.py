# this file is used to push the status update to the rabbitMQ queue

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
  return render_template("fairprice.html")

@app.route("/postStatusUpdate", methods=['GET', 'POST'])
def postStatusUpdate():
  try:
    orderID = request.form['orderID']
    message = request.form['message']
    message_dict = {
      "orderID": orderID,
      "message": message
    }
    message = json.dumps(message_dict)

    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='order.status', body=message, properties=pika.BasicProperties(delivery_mode = 2))
    print(" [x] Sent order status to Order_Status queue: %r" % message)

    return message
  
  except Exception as e:
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='order.error', body=str(e), properties=pika.BasicProperties(delivery_mode = 2))
    print(" [x] Sent order status to Error queue: %r" % str(e))
    
    return "Error: " + str(e)
  
if __name__ == '__main__':
  app.run(port=5100, debug=True)

# use the below code to change data inside message_string
# '{"orderID": "201", "status": "Pending", "message": "Supermarket has been informed of your order"}'
# '{"orderID": "202", "status": "Processing", "message": "Supermarket is preparing your order"}'
# '{"orderID": "203", "status": "In Transit", "message": "Your order is on its way"}'
# '{"orderID": "204", "status": "Delivered", "message": "Your order has been delivered"}'
# '{"orderID": "205", "status": "Cancelled", "message": "Your order has been cancelled"}'