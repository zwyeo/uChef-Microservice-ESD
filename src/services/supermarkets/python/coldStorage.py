from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/coldStorage'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

class SupermarketStock(db.Model):
  __tablename__ = 'coldStorageStock'

  id = db.Column(db.Integer, primary_key=True)
  itemName = db.Column(db.String(50), nullable=False)
  quantity = db.Column(db.Integer)
  price = db.Column(db.Float(precision=2), nullable=False)
  
  def __init__(self, itemName, quantity, price):
    self.itemName = itemName
    self.quantity = quantity
    self.price = price

  def json(self):
    return {"itemName": self.itemName, "price": self.price, "quantity": self.quantity}

@app.route("/supermarketStock")
def get_all():
  stocklist = SupermarketStock.query.all()
  if len(stocklist):
    return jsonify(
      {
        "code": 200,
        "data": {
          "stock": [stock.json() for stock in stocklist]
        }
      }
    )
  return jsonify(
      {
          "code": 404,
          "message": "There are no stocks."
      }
  ), 404


@app.route("/supermarketStock/<string:itemName>")
def find_by_itemName(itemName):
  stock = SupermarketStock.query.filter_by(itemName=itemName).first()
  if stock:
    return jsonify(
        {
          "code": 200,
          "data": stock.json()
        }
    )
  return jsonify(
    {
      "code": 404,
      "message": "Stock not found."
    }
  ), 404


@app.route("/supermarketStock", methods=['POST'])
def create_stock(itemName):
  if (SupermarketStock.query.filter_by(itemName=itemName).first()):
    return jsonify(
      {
        "code": 400,
        "data": {
          "itemName": itemName
        },
        "message": "Stock already exists."
      }
    ), 400

  data = request.get_json()
  stock = SupermarketStock(itemName, **data)

  try:
    db.session.add(stock)
    db.session.commit()
  except:
    return jsonify(
      {
        "code": 500,
        "data": {
          "itemName": itemName
        },
        "message": "An error occurred creating the stock."
      }
    ), 500

  return jsonify(
    {
      "code": 201,
      "data": stock.json()
    }
  ), 201


@app.route("/supermarketStock/<string:itemName>", methods=['PUT'])
def update_stock(itemName):
  stock = SupermarketStock.query.filter_by(itemName=itemName).first()
  if stock:
    data = request.get_json()
    if data['price']:
      stock.price = data['price']
    if data['quantity']:
      stock.quantity = data['quantity']
    db.session.commit()
    return jsonify(
      {
        "code": 200,
        "data": stock.json()
      }
    )
  return jsonify(
    {
      "code": 404,
      "data": {
        "itemName": itemName
      },
      "message": "Stock not found."
    }
  ), 404


@app.route("/supermarketStock/<string:itemName>", methods=['DELETE'])
def delete_stock(itemName):
  stock = SupermarketStock.query.filter_by(itemName=itemName).first()
  if stock:
    db.session.delete(stock)
    db.session.commit()
    return jsonify(
      {
        "code": 200,
        "data": {
          "itemName": itemName
        }
      }
    )
  return jsonify(
    {
      "code": 404,
      "data": {
        "itemName": itemName
      },
      "message": "Stock not found."
    }
  ), 404

if __name__ == '__main__':
    app.run(port=5002, debug=True)
