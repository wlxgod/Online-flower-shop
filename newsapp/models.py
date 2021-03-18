from newsapp import db
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    identity = db.Column(db.String(8))
    password_hash = db.Column(db.String(128))
    flower = db.relationship('Flower', backref='owner', lazy='dynamic')
    order = db.relationship('Order', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Flower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    intro = db.Column(db.String(1000))
    price = db.Column(db.Float)
    number = db.Column(db.Integer)
    img = db.Column(db.String(256))
    address = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestemp = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    price = db.Column(db.Float) # 总价
    destination = db.Column(db.String(256)) # 买家地址
    state = db.Column(db.String(64)) # 订单状态
    number = db.Column(db.Integer) # 数量
    way = db.Column(db.String(16)) # 提货方式，快递或者自提
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    flower = db.relationship('Flower', backref='order', lazy='dynamic') # 货物
