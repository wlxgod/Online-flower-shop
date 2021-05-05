from newsapp.models import Orders
from newsapp import db
import datetime

def CreateOrder():
    orderA= Orders(id=8,timestamp=datetime.datetime.now(),price=32,name="Abraham",destination="233/44, Los Vagas Str.",state="Lated",number="4",way="logistic",user_id=1)
    orderB= Orders(id=9,timestamp=datetime.datetime.fromtimestamp(1616672048),price=43,name="Abey",destination="233/44, Los Vagas Str.",state="Completed",number="4",way="logistic",user_id=1)
    orderC= Orders(id=64,timestamp=datetime.datetime.fromtimestamp(1578053401),price=288,name="EisenHower",destination="233/44, Los Vagas Str.",state="Completed",number="4",way="logistic",user_id=1)
    orderD= Orders(id=81,timestamp=datetime.datetime.fromtimestamp(1578053401),price=648,name="Lincoln",destination="233/44, Los Vagas Str.",state="Transporting",number="4",way="logistic",user_id=1)
    db.session.add(orderA)
    db.session.add(orderB)
    db.session.add(orderC)
    db.session.add(orderD)

    db.session.commit()