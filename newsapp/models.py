import datetime

from newsapp import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    identity = db.Column(db.String(8))
    password_hash = db.Column(db.String(128))
    orders = db.relationship('Orders', backref='owner', lazy='dynamic')
    basket = db.relationship('Basket', backref='user_basket', lazy='dynamic')
    basketlike = db.relationship('Basketlike', backref='user_basketlike1', lazy='dynamic')
    want = db.relationship('Want', backref='user_want', lazy='dynamic')
    sender = db.relationship('Message', backref='sender', lazy='dynamic')
    news = db.relationship('News', backref='user', lazy='dynamic')
    profile = db.relationship('Profile', backref='profile', lazy='dynamic')
    review = db.relationship('Review', backref='user', lazy='dynamic')

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
    img1 = db.Column(db.String(256))
    address = db.Column(db.String(256))
    basket = db.relationship('Basket', backref='flower_basket', lazy='dynamic')  # 货物
    basketlike = db.relationship('Basketlike', backref='flower_basketlike', lazy='dynamic')  # 货物"""

# 我想要
class Want(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    basketlike = db.relationship('Basketlike', backref='flower_basketlike2', lazy='dynamic')  # 货物

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow())
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
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))

# 喜欢单品
class Basketlike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)  # 鲜花名字
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    flower_id = db.Column(db.Integer, db.ForeignKey('flower.id'))  # 鲜花id
    want_id = db.Column(db.Integer, db.ForeignKey('want.id'))

# 资料
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    dob = db.Column(db.String(30))
    gender = db.Column(db.Integer)
    description = db.Column(db.String(250))
    portrait = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    news_id = db.relationship('News', backref='profile', lazy='dynamic')
    review_id = db.relationship('Review', backref='profile', lazy='dynamic')


# 留言消息
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500))  # 消息
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now)  # 时间
    state = db.Column(db.String(10))  # 状态，未读或已读
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 发送
    receiver_id = db.Column(db.Integer)  # 接收

    # 用于将queryset转化为字典，用json传输到前台
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

# 新消息数量
# 顾客每发一条消息，数量加一，客服阅读后归0
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, default=0)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver_id = db.Column(db.Integer)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))

# 商品评论
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rate = db.Column(db.Integer, default=0)    # 等级
    text = db.Column(db.String(250))    # 评论
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    flower_id = db.Column(db.Integer)

