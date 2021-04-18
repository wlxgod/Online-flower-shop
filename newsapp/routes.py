import os
import string

from flask import render_template, flash, redirect, url_for, session, request, jsonify
from sqlalchemy import and_,or_
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from newsapp import app, db, config
from newsapp.forms import LoginForm, SignupForm, FlowerForm
from newsapp.models import Flower, Order, Basket,Message,Profile,News
from newsapp.models import User


@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        if form.password.data != form.password2.data:
            flash('Passwords do not match!')
            return redirect(url_for('signup'))
        passw_hash = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password_hash=passw_hash)
        db.session.add(user)
        db.session.commit()
        session["USERNAME"] = user.username
        return redirect('login')
    return render_template('signup.html', title='Register a new user', form=form)


@app.route('/signupch', methods=['GET', 'POST'])
def signupch():
    form = SignupForm()
    if form.validate_on_submit():
        if form.password.data != form.password2.data:
            flash('Passwords do not match!')
            return redirect(url_for('signup'))
        passw_hash = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password_hash=passw_hash)
        db.session.add(user)
        db.session.commit()
        session["USERNAME"] = user.username
        return redirect('login')
    return render_template('signupCh.html', title='新用户注册', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user is None:
            flash("Please Register or Retry With a Valid Username")
            return redirect(url_for('login'))
        if not check_password_hash(user.password_hash, form.password.data):
            flash('Wrong Password')
            return redirect(url_for('login'))
        flash('Login Successfully')
        session['USERNAME'] = user.username
        return redirect('index')
    return render_template('login.html', title='Log in', form=form)


@app.route('/loginch', methods=['GET', 'POST'])
def loginch():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user is None:
            flash("Please Register or Retry With a Valid Username")
            return redirect(url_for('login'))
        if not check_password_hash(user.password_hash, form.password.data):
            flash('Wrong Password')
            return redirect(url_for('login'))
        flash('Login Successfully')
        session['USERNAME'] = user.username
        return redirect('index')
    return render_template('loginCh.html', title='登录', form=form)




# new index page!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@app.route('/index', methods=['GET', 'POST'])
def index():
    """flower = Flower(name="rose", intro="DO the test", price=100,
                    number=50, img="signup.jfif" ,address="CHINESE FOREVER ROAD")
    db.session.add(flower)
    db.session.commit()"""
    """form=SearchForm()"""
    posts_query = Flower.query
    posts = posts_query.filter().all()
    posts2 = posts
    username = session.get("USERNAME")
    user = User.query.filter(User.username == username).first()
    user_id = user.id
    order_in_db = Order.query.filter(and_(Order.state == "unpayment", Order.user_id == user_id)).first()
    if order_in_db is None:
        order = Order(price=0, name=user.username, destination="Beijing university of technology",
                      state="unpayment", number=100, way="deliver", user_id=user.id)
        db.session.add(order)
        db.session.commit()
    order_in_db = Order.query.filter(and_(Order.state == "unpayment", Order.user_id == user_id)).first()
    basket_in_db_list = Basket.query.filter(and_(Basket.order_id == order_in_db.id, Basket.user_id == user_id)).all()
    basket_length = len(basket_in_db_list)
    '''print(posts)'''
    total = 0
    for basket in basket_in_db_list:
        total = total + basket.total*basket.quantity
    content = None
    content = request.form.get('content')
    print(content)
    if content is not None and content != "搜索" and content!="":
        posts2 = Flower.query.filter(Flower.name == content).all()
        content = ""
    print(posts2)
    print(posts)
    return render_template('newindex.html', posts=posts, baskets=basket_in_db_list, length=basket_length, total=total,
                           order=order_in_db, posts2=posts2)


# new index page!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@app.route('/indexch', methods=['GET', 'POST'])
def indexch():
    """flower = Flower(name="rose", intro="DO the test", price=100,
                    number=50, img="signup.jfif" ,address="CHINESE FOREVER ROAD")
    db.session.add(flower)
    db.session.commit()"""
    """form=SearchForm()"""
    posts_query = Flower.query
    posts = posts_query.filter().all()
    posts2 = posts
    username = session.get("USERNAME")
    user = User.query.filter(User.username == username).first()
    user_id = user.id
    order_in_db = Order.query.filter(and_(Order.state == "unpayment", Order.user_id == user_id)).first()
    if order_in_db is None:
        order = Order(price=0, name=user.username, destination="Beijing university of technology",
                      state="unpayment", number=100, way="deliver", user_id=user.id)
        db.session.add(order)
        db.session.commit()
    order_in_db = Order.query.filter(and_(Order.state == "unpayment", Order.user_id == user_id)).first()
    basket_in_db_list = Basket.query.filter(and_(Basket.order_id == order_in_db.id, Basket.user_id == user_id)).all()
    basket_length = len(basket_in_db_list)
    '''print(posts)'''
    total = 0
    for basket in basket_in_db_list:
        total = total + basket.total
    content = None
    content = request.form.get('content')
    print(content)
    if content is not None and content != "搜索" and content!="":
        posts2 = Flower.query.filter(Flower.name == content).all()
        content = ""
    print(posts2)
    print(posts)
    return render_template('newindexCh.html', posts=posts, baskets=basket_in_db_list, length=basket_length, total=total,
                           order=order_in_db, posts2=posts2)


# 原来的category页面
@app.route('/shop', methods=['GET', 'POST'])
def shop():
    """flower = Flower(name="rose", intro="DO the test", price=100,
                    number=50, img="signup.jfif" ,address="CHINESE FOREVER ROAD")
    db.session.add(flower)
    db.session.commit()"""
    posts_query = Flower.query
    posts = posts_query.filter().all()
    username = session.get("USERNAME")
    user = User.query.filter(User.username == username).first()
    user_id = user.id
    order_in_db = Order.query.filter(and_(Order.state == "unpayment", Order.user_id == user_id)).first()
    if order_in_db is None:
        order = Order(price=0, name=user.username, destination="Beijing university of technology",
                      state="unpayment", number=100, way="deliver", user_id=user.id)
        db.session.add(order)
        db.session.commit()
    order_in_db = Order.query.filter(and_(Order.state == "unpayment", Order.user_id == user_id)).first()
    basket_in_db_list = Basket.query.filter(and_(Basket.order_id == order_in_db.id, Basket.user_id == user_id)).all()
    basket_length = len(basket_in_db_list)
    '''print(posts)'''
    total = 0
    for basket in basket_in_db_list:
        total = total + basket.total*basket.quantity
    return render_template('newshop.html', posts=posts, baskets=basket_in_db_list, length=basket_length, total=total,
                           order=order_in_db)


@app.route('/shopch', methods=['GET', 'POST'])
def shopch():
    """flower = Flower(name="rose", intro="DO the test", price=100,
                    number=50, img="signup.jfif" ,address="CHINESE FOREVER ROAD")
    db.session.add(flower)
    db.session.commit()"""
    posts_query = Flower.query
    posts = posts_query.filter().all()
    username = session.get("USERNAME")
    user = User.query.filter(User.username == username).first()
    user_id = user.id
    order_in_db = Order.query.filter(and_(Order.state == "unpayment", Order.user_id == user_id)).first()
    if order_in_db is None:
        order = Order(price=0, name=user.username, destination="Beijing university of technology",
                      state="unpayment", number=100, way="deliver", user_id=user.id)
        db.session.add(order)
        db.session.commit()
    order_in_db = Order.query.filter(and_(Order.state == "unpayment", Order.user_id == user_id)).first()
    basket_in_db_list = Basket.query.filter(and_(Basket.order_id == order_in_db.id, Basket.user_id == user_id)).all()
    basket_length = len(basket_in_db_list)
    '''print(posts)'''
    total = 0
    for basket in basket_in_db_list:
        total = total + basket.total
    return render_template('newshopCh.html', posts=posts, baskets=basket_in_db_list, length=basket_length, total=total,
                           order=order_in_db)





@app.route('/detail', methods=['GET', 'POST'])
def detail():
    return render_template('newproduct-details.html')















@app.route("/RemoveBasket",methods=['GET', 'POST'])
def RemoveBasket():
    if session.get("USERNAME") is None:
        return redirect("login")
    else:
        username = session.get("USERNAME")
        user = User.query.filter(User.username == username).first()
        user_id = user.id
        basketId = request.form['id']
        print(basketId)
        basket_in_db = Basket.query.filter(Basket.id == basketId).first()
        db.session.delete(basket_in_db)
        db.session.commit()
        order_in_db = Order.query.filter(and_(Order.state == "unpayment", Order.user_id == user_id)).first()
        basket_in_db_list = Basket.query.filter(
            and_(Basket.order_id == order_in_db.id, Basket.user_id == user_id)).all()
        basket_length = len(basket_in_db_list)
        total = 0
        for basket in basket_in_db_list:
            total = total + basket.total
        return jsonify({'message': 'remove to Trolley successfully!','id': basketId,'length':basket_length,'total':total})


@app.route("/PaymentOrder")
def PaymentOrder():
    if session.get("USERNAME") is None:
        return redirect("login")
    else:
        orderId = int(request.args.get('orderId'))
        username = session.get("USERNAME")
        user = User.query.filter(User.username == username).first()
        user_id = user.id
        order_in_db = Order.query.filter(
            and_(Order.state == "unpayment", Order.user_id == user_id, Order.id == orderId)).first()
        order_in_db.state = "Transporting"
        db.session.commit()
        order = Order(price=0, name=user.username, destination="Beijing university of technology",
                      state="unpayment", number=100, way="deliver", user_id=user.id)
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('index'))


@app.route("/addToCart",methods=['GET', 'POST'])
def addToCart():
    if session.get("USERNAME") is None:
        return redirect("login")
    else:
        username = session.get("USERNAME")
        user = User.query.filter(User.username == username).first()
        user_id = user.id
        orders_in_db = Order.query.filter(Order.user_id == user_id).all()
        flag = 1
        if orders_in_db is not None:
            for order in orders_in_db:
                if order.state == 'unpayment':
                    flag = 0
        else:
            flag = 1
        if flag == 1:
            order = Order(price=0, name=user.username, destination="Beijing university of technology",
                          state="unpayment", number=100, way="deliver", user_id=user.id)
            db.session.add(order)
            db.session.commit()
        productId = request.form['id']
        quantity=request.form['quantity']
        flowername=request.form['name']
        print(productId)
        print(flowername)
        if productId!='100':
            flower_in_db = Flower.query.filter(Flower.id == productId).first()
        else:
            flower_in_db = Flower.query.filter(Flower.name == flowername).first()
        order_id = Order.query.filter(and_(Order.state == "unpayment", Order.user_id == user_id)).first().id
        basket = Basket(name=flower_in_db.name, quantity=quantity, total=flower_in_db.price, user_id=user_id,
                        flower_id=flower_in_db.id, order_id=order_id)
        basketImg = flower_in_db.img
        basketQuantity=basket.quantity
        basketTotal=int(basket.total)*int(quantity)
        db.session.add(basket)
        db.session.commit()
        order_in_db = Order.query.filter(and_(Order.state == "unpayment", Order.user_id == user_id)).first()
        order_in_db.price = order_in_db.price + basket.total*basket.quantity
        print("order_in_db.price_after:")
        print(order_in_db.price)
        db.session.commit()
        order_in_db = Order.query.filter(and_(Order.state == "unpayment", Order.user_id == user_id)).first()
        basket_in_db_list = Basket.query.filter(
            and_(Basket.order_id == order_in_db.id, Basket.user_id == user_id)).all()
        basket_length = len(basket_in_db_list)
        basketId=basket_length
        print(basketId)
        """order_in_db = Order.query.filter(and_(Order.state == "unpayment", Order.user_id == user_id)).first()
        print(order_in_db.price)"""
        return jsonify({'message': 'Add to Trolley successfully!','length':basket_length,'id': basketId,'img':basketImg,'quantity':basketQuantity,'total':basketTotal})



@app.route('/checkout')
def checkout():
    return render_template('checkout.html')


@app.route('/complete')
def complete():
    return render_template('complete.html')


@app.route('/about_us')
def about_us():
    return render_template('newabout_us.html')


@app.route('/logout')
def logout():
    if session['USERNAME'] is None:
        return redirect(url_for('signup'))
    session.pop("USERNAME", None)
    return redirect(url_for('signup'))


@app.route('/addflower', methods=['GET', 'POST'])
def addflower():
    form = FlowerForm()
    if session.get("USERNAME") is None:
        return redirect("login")
    else:
        print("caocaocao1")
        if form.validate_on_submit():
            name = form.name.data
            img_dir = config.Config.PC_UPLOAD_DIR
            print(img_dir)
            img_obj = form.image.data
            img_filename = session.get("USERNAME") + name + '_img.jpg'
            print(os.path.join(img_dir, img_filename))
            img_obj.save(os.path.join(img_dir, img_filename))
            flower = Flower(name=form.name.data, intro=form.detail.data, price=form.price.data, number=form.number.data,
                            img=img_filename, address=form.address.data)
            print("caocaocao3")
            db.session.add(flower)
            db.session.commit()
            flash("'Add flower successfully!")
            return redirect(url_for('index'))
        else:
            return render_template('addFlowers.html', title='add flowers', form=form)


@app.route('/checkusername', methods=['POST'])
def check_username():
    chosen_name = request.form['username']
    user_in_db = User.query.filter(User.username == chosen_name).first()
    if not user_in_db:
        return jsonify({'text': 'Username is available',
                        'returnvalue': 0})
    else:
        return jsonify({'text': 'Username is already taken',
                        'returnvalue': 1})


@app.route('/checkemail', methods=['POST'])
def check_email():
    chosen_email = request.form['email']
    user_in_db = User.query.filter(User.email == chosen_email).first()
    if not user_in_db:
        return jsonify({'text': 'This Email is available',
                        'returnvalue': 0})
    else:
        return jsonify({'text': 'This Email is already taken',
                        'returnvalue': 1})


@app.route('/OrderDisplay', methods=['GET', 'POST'])
def OrderDisplay():
    orders = Order.query.all()
    order = Order.query.filter(Order.id == 1)
    return render_template('OrderDisplay.html', title='Order Display', orders=orders, order=order)


@app.route('/OrderDetail/<order_id>', methods=['GET', 'POST'])
def OrderDetail(order_id):
    order = Order.query.filter(Order.id == order_id).first()
    user = User.query.filter(User.id == order.user_id).first()
    orders = Order.query.filter(Order.user_id == user.id)
    flowers = Flower.query.all()
    baskets = Basket.query.filter(Basket.order_id == order_id)
    total = 0
    for basket in baskets:
        total = total + basket.total
    return render_template('OrderDetail.html', title='Order Display', order=order, flowers=flowers, orders=orders,
                           total=total, baskets=baskets)

@app.route('/Modify/<flower_id>', methods=['GET', 'POST'])
def Modify(flower_id):
    flower = Flower.query.filter(Flower.id == flower_id).first()
    flowers = Flower.query.all()
    if request.method == 'POST':
        if request.values.get('t'):
            print(request.values.get('t'))
            print(request.values.get('price'))
            # file_obj = request.files.get('photos')
            # print(file_obj)
            img_dir = config.Config.PC_UPLOAD_DIR
            # print(img_dir)
            # img_filename = '1'
            # print(os.path.join(img_dir, img_filename))

            # print(secure_filename(file_obj.filename))
            flower.name = request.values.get('name')
            flower.intro = request.values.get('detail')
            flower.price = request.values.get('price')
            if request.files.get("photos") != 'null':
                file_obj = request.files.get('photos')
                file_name = secure_filename(file_obj.filename)
                file_obj.save(os.path.join(img_dir, file_name))
                flower.img = file_name
            flower.number = request.values.get('avail')
            db.session.commit()
            return redirect(url_for('Flowers'))
    if request.method == 'GET':
        print(request.method)
        return redirect(url_for('Flowers'))

@app.route('/ModifyFlower/<flower_id>', methods=['GET', 'POST'])
def ModFlower(flower_id):
    flower = Flower.query.filter(Flower.id == flower_id).first()
    return render_template('ModifyFlower.html', title='FlowersChange', flower=flower)


@app.route('/FlowerGallery', methods=['GET', 'POST'])
def Flowers():
    flowers = Flower.query.all()
    return render_template('FlowerGallery.html', title='Flowers', flowers=flowers)



@app.route('/ChatRoom', methods=['GET', 'POST'])
def ChatRoom():
    staff = User.query.filter(User.username == session['USERNAME']).first().id  # 自己的id
    img = Profile.query.filter(Profile.user_id == staff).first().portrait     # 头像
    # 获取历史聊天用户和新消息数量
    new = News.query.filter(News.staff_id == staff).order_by(News.number.desc())
    return render_template('ChatRoom.html', title='ChatRoom', news=new, img=img)


@app.route('/shownews', methods=['GET', 'POST'])
def shownews():
    id1 = User.query.filter(User.username == session['USERNAME']).first().id  # 自己的id
    id2 = request.form['user_id']  # 顾客的id
    print(id1)
    print(id2)
    user_news = News.query.filter(and_(News.user_id == id2, News.staff_id == id1)).first()
    user_news.number = 0  # 未读消息归0
    db.session.commit()
    message = Message.query.filter(or_((and_(Message.sender_id == id1, Message.receiver_id == id2)),
                                       (and_(Message.sender_id == id2, Message.receiver_id == id1)))).order_by(
        Message.timestamp)  # 聊天记录和新消息
    print(message.count())
    news = []
    # 转化为字典list
    for new in message:
        news.append(new.to_json())
    print(len(news))
    return jsonify(news)


@app.route('/sendnew', methods=['POST'])
def sendnew():
    receiver_id = request.form['receiver_id'] # 接受者
    text = request.form['text']     # 消息
    user_id = User.query.filter(User.username == session['USERNAME']).first().id # 发送者
    message = Message(text=text, sender_id=user_id, receiver_id=receiver_id, state='read') # 写入新消息
    news = News.query.filter(and_(News.user_id == user_id, News.staff_id == receiver_id)).first()    # 查找新消息数量的记录
    print(user_id)
    profile_id = Profile.query.filter(Profile.user_id == user_id).first().id      # 发送者资料的id
    if not news:
        news = News(number=1, user_id=user_id, staff_id=receiver_id, profile_id=profile_id)
        db.session.add(news)
    else:
        news.number = news.number+1               # 新消息加一
    db.session.add(message)
    db.session.commit()
    return jsonify({'state': 'yes'})


@app.route('/current_user', methods=['GET', 'POST'])
def current_user():
    user_id = User.query.filter(User.username == session['USERNAME']).first().id
    return jsonify({'id': user_id})
@app.route('/Delete/<flower_id>', methods=['GET', 'POST'])
def Delete(flower_id):
    flower = Flower.query.filter(Flower.id == flower_id).first()
    flowers = Flower.query.all()
    if request.method == 'POST':
        if request.values.get('d'):
            print(request.values.get('d'))
            db.session.delete(flower)
            db.session.commit()
            return render_template('FlowerGallery.html', title='Flowers', flowers=flowers)
    return render_template('FlowerGallery.html', title='Flowers', flowers=flowers)


@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ModifyOrder/<order_id>', methods=['GET', 'POST'])
def ModifyOrder(order_id):
    order = Order.query.filter(Order.id == order_id).first()
    return render_template('ModifyOrder.html', title='ModifyOrder', order=order)


@app.route('/Order_state_C/<order_id>', methods=['GET', 'POST'])
def Order_state_C(order_id):
    order = Order.query.filter(Order.id == order_id).first()
    order.state = 'Completed'
    db.session.commit()
    return redirect(url_for('ModifyOrder', order_id=order.id))


@app.route('/Order_state_T/<order_id>', methods=['GET', 'POST'])
def Order_state_T(order_id):
    order = Order.query.filter(Order.id == order_id).first()
    order.state = 'Transporting'
    db.session.commit()
    return redirect(url_for('ModifyOrder', order_id=order.id))


@app.route('/Order_state_L/<order_id>', methods=['GET', 'POST'])
def Order_state_L(order_id):
    order = Order.query.filter(Order.id == order_id).first()
    order.state = 'Lated'
    db.session.commit()
    return redirect(url_for('ModifyOrder', order_id=order.id))


@app.route('/Order_Delete/<order_id>', methods=['GET', 'POST'])
def Order_Delete(order_id):
    order = Order.query.filter(Order.id == order_id).first()
    orders = Order.query.all()
    if request.method == "POST":
        if request.values.get('d'):
            db.session.delete(order)
            db.session.commit()
            return redirect(url_for('OrderDisplay'))
        return redirect(url_for('OrderDisplay'))
    return redirect(url_for('OrderDisplay'))


@app.route('/Change_Address/<order_id>', methods=['GET', 'POST'])
def Change_Address(order_id):
    order = Order.query.filter(Order.id == order_id).first()
    print(request.values.get('text'))
    print(request.values.get('c'))
    if request.method == 'POST':
        if request.values.get('c'):
            order.destination = request.values.get('text')
            db.session.commit()
            return redirect(url_for('ModifyOrder', order_id=order.id))
    if request.method == 'GET':
        print(request.method)
        return redirect(url_for('ModifyOrder', order_id=order.id))

