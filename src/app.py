from flask import Flask, redirect, request

import stripe


app = Flask(__name__)

@app.route('/')
def test():
    print('Hello from stripe')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
