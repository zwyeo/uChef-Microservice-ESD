from flask import Flask, redirect, request

import stripe
from torch import device

app = Flask(__name__)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
