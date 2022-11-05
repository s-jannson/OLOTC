from datetime import datetime
from functools import total_ordering

from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///olotc.sqlite3'
app.config['SECRET_KEY'] = "random-secret-strong-string"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

class trade(db.Model):
    id = db.Column('entry_id', db.Integer, primary_key = True)
    datetime = db.Column(db.DateTime, nullable=False)
    price_usd = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    total_value = db.Column(db.Float, nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, datetime, price_usd, quantity, total_value):
        self.datetime = datetime
        self.price_usd = float(price_usd)
        self.quantity = float(quantity)
        self.total_value = total_value


@app.route('/api/', methods=['GET'])
@cross_origin()
def get_all_trades():
    trades = trade.query.order_by(trade.datetime).all()
    output = []
    for t in trades:
        trade_data = {'datetime': t.datetime.strftime('%Y-%m-%dT%H:%M:%S.%fZ'), 'price_usd': t.price_usd, 'quantity': t.quantity, 'total_value': t.total_value}
        output.append(trade_data)
    return jsonify(output)

@app.route('/api/new', methods = ['POST'])
@cross_origin()
def new_otc_trade():
    data = request.get_json()
    if not data['datetime'] or not data['price'] or not data['quantity']:
        return Response(
            "Missing body parameters",
            status=400,
        )
    else:
        if not data_validated(data):
            return Response(
                "Invalid body parameters",
                status=400,
            )
        _datetime = datetime.strptime(data['datetime'], '%Y-%m-%dT%H:%M:%S.%fZ')
        total_value = float(data['price']) * float(data['quantity'])
        new_trade = trade(datetime=_datetime, price_usd=data['price'], quantity=data['quantity'], total_value=total_value)
        db.session.add(new_trade)
        db.session.commit()
        print('New trade was added successfully')
        return Response('ok', status=201)

def data_validated(data):
    try:
        d = datetime.strptime(data['datetime'], '%Y-%m-%dT%H:%M:%S.%fZ')
        p = float(data['price'])
        q = float(data['quantity'])
    except ValueError:
        return False
    if p <= 0 or q <= 0:
        return False
    if d > datetime.now():
        return False
    return True


if __name__ == '__main__':
   with app.app_context():
    db.create_all()
   app.run()
