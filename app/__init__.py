from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


#   database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()



from app import views
from app.db import user_model