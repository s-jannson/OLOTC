from datetime import datetime
from functools import total_ordering

from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///olotc.sqlite3'
app.config['SECRET_KEY'] = "random-secret-strong-string"

db = SQLAlchemy(app)

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


@app.route('/', methods=['GET'])
def get_all_trades():
    trades = trade.query.all()
    output = []
    for t in trades:
        trade_data = {'datetime': t.datetime, 'price_usd': t.price_usd, 'quantity': t.quantity, 'total_value': t.total_value}
        output.append(trade_data)
    return jsonify(output)

@app.route('/new', methods = ['POST'])
def new_otc_trade():
    data = request.get_json()
    if not data['datetime'] or not data['price'] or not data['quantity']:
        return Response(
            "Missing body parameters",
            status=400,
        )
    else:
        _datetime = datetime.strptime(data['datetime'], '%Y-%m-%dT%H:%M:%S')
        total_value = float(data['price']) * float(data['quantity'])
        new_trade = trade(datetime=_datetime, price_usd=data['price'], quantity=data['quantity'], total_value=total_value)
        db.session.add(new_trade)
        db.session.commit()
        print('New trade was added successfully')
        return Response('ok', status=201)

if __name__ == '__main__':
   with app.app_context():
    db.create_all()
   app.run()