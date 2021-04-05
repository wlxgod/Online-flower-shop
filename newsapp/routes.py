import os

from flask import render_template, flash, redirect, url_for, session, request, jsonify
from sqlalchemy import and_
from werkzeug.security import generate_password_hash, check_password_hash

from newsapp import app, db, config
from newsapp.forms import LoginForm, SignupForm, FlowerForm
from newsapp.models import Flower, Order, Basket
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
        total = total + basket.total
    content = None
    content = request.form.get('content')
    print(content)
    if content is not None and content != "搜索" and content!="":
        posts2 = Flower.query.filter(Flower.name == content).all()
        content = ""
    print(posts2)
    print(posts)
    return render_template('index.html', posts=posts, baskets=basket_in_db_list, length=basket_length, total=total,
                           order=order_in_db, posts2=posts2)


@app.route("/RemoveBasket")
def RemoveBasket():
    if session.get("USERNAME") is None:
        return redirect("login")
    else:
        basketId = int(request.args.get('basketId'))
        basket_in_db = Basket.query.filter(Basket.id == basketId).first()
        db.session.delete(basket_in_db)
        db.session.commit()
        return redirect(url_for('index'))


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


@app.route("/addToCart")
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
        productId = int(request.args.get('productId'))
        print(productId)
        flower_in_db = Flower.query.filter(Flower.id == productId).first()
        order_id = Order.query.filter(and_(Order.state == "unpayment", Order.user_id == user_id)).first().id
        print(flower_in_db.name + " " + flower_in_db.address)
        basket = Basket(name=flower_in_db.name, quantity=1, total=flower_in_db.price, user_id=user_id,
                        flower_id=flower_in_db.id, order_id=order_id)
        db.session.add(basket)
        db.session.commit()
        order_in_db = Order.query.filter(and_(Order.state == "unpayment", Order.user_id == user_id)).first()
        order_in_db.price = order_in_db.price + basket.total
        db.session.commit()
        """order_in_db = Order.query.filter(and_(Order.state == "unpayment", Order.user_id == user_id)).first()
        print(order_in_db.price)"""
        return redirect(url_for('index'))


@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    return render_template('contact_us.html')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/category', methods=['GET', 'POST'])
def category():
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
    return render_template('category.html', posts=posts, baskets=basket_in_db_list, length=basket_length, total=total,
                           order=order_in_db)


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


@app.route('/profile')
def profile():
    return render_template('profile.html')
