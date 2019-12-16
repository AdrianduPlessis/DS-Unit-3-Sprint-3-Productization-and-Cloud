"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import openaq
import aq_functions

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(APP)

class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return f"<br>Time {self.datetime} --- Value {self.value}"


@APP.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    
    # Get data from OpenAQ
    response = aq_functions.get_latest_observations()

    # Make Record objects with it and add to db
    for record in response:
    	db_record = Record(datetime=record[0], value=record[1])
    	DB.session.add(db_record)


    DB.session.commit()
    return 'Data refreshed!'



@APP.route('/')
def root():
    """Base view."""
    danger = Record.query.filter(Record.value >= 10).all()
    return str(danger)



