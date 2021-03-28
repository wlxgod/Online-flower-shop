import datetime

from newsapp import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    identity = db.Column(db.String(8))
    password_hash = db.Column(db.String(128))
    order = db.relationship('Order', backref='owner', lazy='dynamic')
    basket = db.relationship('Basket', backref='user_basket', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staffname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    identity = db.Column(db.String(8))
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Staff {}>'.format(self.staffname)


class Flower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    intro = db.Column(db.String(1000))
    price = db.Column(db.Float)
    number = db.Column(db.Integer)
    img = db.Column(db.String(256))
    address = db.Column(db.String(256))
    basket = db.relationship('Basket', backref='flower_basket', lazy='dynamic')  # 货物


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestemp = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    price = db.Column(db.Float)  # 总价
    name = db.Column(db.String(64))  # 买家姓名
    destination = db.Column(db.String(256))  # 买家地址
    state = db.Column(db.String(64))  # 订单状态
    number = db.Column(db.Integer)  # 数量
    way = db.Column(db.String(16))  # 提货方式，快递或者自提
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    basket = db.relationship('Basket', backref='order_basket', lazy='dynamic')


# 购物车
class Basket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)  # 鲜花名字
    quantity = db.Column(db.Integer, index=True)  # 数量
    total = db.Column(db.Integer, index=True)  # 总价
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    flower_id = db.Column(db.Integer, db.ForeignKey('flower.id'))  # 鲜花id
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
