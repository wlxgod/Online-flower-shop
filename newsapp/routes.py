import os
import time,datetime

from flask import render_template, flash, redirect, url_for, session, request, jsonify, Config
from werkzeug.security import generate_password_hash, check_password_hash

from newsapp import app, db, config
from newsapp.forms import LoginForm, SignupForm, FlowerForm
from newsapp.models import Flower, Order, Basket
from newsapp.models import User


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
        return redirect('addflower')
    return render_template('signup.html', title='Register a new user', form=form)


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
        return redirect('choice')
    return render_template('login.html', title='Log in', form=form)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    """flower = Flower(name="rose", intro="DO the test", price=100,
                    number=50, img="signup.jfif" ,address="CHINESE FOREVER ROAD")
    db.session.add(flower)
    db.session.commit()"""
    posts_query=Flower.query
    posts=posts_query.filter().first()
    print(posts)
    return render_template('index.html', posts=posts)


@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    return render_template('contact_us.html')


@app.route('/category', methods=['GET', 'POST'])
def category():
    return render_template('category.html')


'''@app.route('/logout')
def logout():
    if session['USERNAME'] is None:
        return redirect(url_for('signup'))
    session.pop("USERNAME", None)
    return redirect(url_for('signup'))'''


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
            flower = Flower(name=form.name.data, intro=form.detail.data, price=form.price.data, number=form.number.data,img=img_filename, address=form.address.data)
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
    print(orders[1].timestamp.strftime("%Y/%m/%d"))
    #just output the date
    for order in orders:
        order.timestamp = order.timestamp.strftime("%Y/%m/%d")

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
        total = total+basket.total
    return render_template('OrderDetail.html', title='Order Display', order=order, flowers=flowers, orders=orders, total=total, baskets=baskets)


@app.route('/OrderDetailT', methods=['GET', 'POST'])
def OrderDetailT():

    return render_template('OrderDetailT.html')