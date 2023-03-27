#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script
# monitor status log queue in rabbitMQ

import json
import os

import amqp_setup
import fcm_cloud_messaging as fcm_pusher
# import delivery_status_firebase as db

monitorBindingKey='*.status'

def receiveStatusLog():
    amqp_setup.check_setup()
        
    queue_name = 'Status'
    
    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 
    #it doesn't exit by default. Use Ctrl+C in the command window to terminate it.

def callback(channel, method, properties, body): # required signature for the callback; no return
    print("\nReceived an status log by " + __file__)
    body_dict = json.loads(body)
    processStatusLog(body_dict)

    fcm_pusher.sendPush("System Notification", "Order Update for order ID: {}, status: {}".format(body_dict['orderID'],body_dict['message']))
    # db.updateDatabase(body_dict)

    print() # print a new line feed

def processStatusLog(status):
    print("Recording an status log:")
    print(status)


if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    receiveStatusLog()