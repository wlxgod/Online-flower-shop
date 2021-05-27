from newsapp import app,db

if __name__ == '__main__':
    """db.drop_all()
    db.create_all()"""
    db.create_all()
    # test.CreateOrder()
    app.run(debug=True)
