"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask
import openaq
import aq_functions

APP = Flask(__name__)
api = openaq.OpenAQ()

@APP.route('/')
def root():
    """Base view."""
    response = aq_functions.get_latest_observations()
    return str(response)



