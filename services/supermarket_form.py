# this file is used to push the status update to the rabbitMQ queue

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

import amqp_setup
import pika
import json
import datetime

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
  return render_template("deliveryStatus.html")

@app.route("/postStatusUpdate", methods=['GET', 'POST'])
def postStatusUpdate():
  try:
    orderID = request.form['orderID']
    message = request.form['message']
    message_dict = {
      "orderID": orderID,
      "message": message,
      "time": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
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

# use the below code as reference data for the message
# '{"orderID": "201", "message": "Supermarket has been informed of your order"}'
# '{"orderID": "202", "message": "Supermarket is preparing your order"}'
# '{"orderID": "203", "message": "Your order is on its way"}'
# '{"orderID": "204", "message": "Your order has been delivered"}'
# '{"orderID": "205", "message": "Your order has been cancelled"}'