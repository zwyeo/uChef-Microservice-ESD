from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

app = Flask(__name__)
CORS(app)

order_URL = "http://localhost:5002/order"
fairprice_URL = "http://localhost:5003/fairPrice"
coldStorage_URL = "http://localhost:5004/coldStorage"
payment_URL = "http://localhost:5005/payment"
notification_url = "http://localhost:5006/notification"
error_url = "http://localhost:5007/error"
recipe = "http://localhost:5008/recipe"
orderStatus = "http://localhost:5009/orderStatus"


