import sqlalchemy
from flask import Flask
from newsapp.config import Config

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from newsapp import routes, models