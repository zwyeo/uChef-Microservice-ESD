# this file is used to push the same status update to the rabbitMQ queue all the time
# default data is found in line 24 (message_string) - edit line 24 to change the data

from flask import Flask, request, jsonify
from flask_cors import CORS

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Please navigate to /postStatusUpdate to post a status update."

@app.route("/postStatusUpdate")
def postStatusUpdate():
  message_string = '{"orderID": "201", "status": "Pending", "message": "Supermarket has been informed of your order"}'
  message_json = json.loads(message_string)
  message = json.dumps(message_json)

  amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='order.status', body=message, properties=pika.BasicProperties(delivery_mode = 2))
  
  print(" [x] Sent order status to Order_Status queue: %r" % message)
  return message

if __name__ == '__main__':
  app.run(port=5100, debug=True)

# use the below code to change data inside message_string
# '{"orderID": "201", "status": "Pending", "message": "Supermarket has been informed of your order"}'
# '{"orderID": "202", "status": "Processing", "message": "Supermarket is preparing your order"}'
# '{"orderID": "203", "status": "In Transit", "message": "Your order is on its way"}'
# '{"orderID": "204", "status": "Delivered", "message": "Your order has been delivered"}'
# '{"orderID": "205", "status": "Cancelled", "message": "Your order has been cancelled"}'