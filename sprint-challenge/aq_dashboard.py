"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask
import openaq

APP = Flask(__name__)
api = openaq.OpenAQ()

@APP.route('/')
def root():
    """Base view."""
    status, body = api.measurements(city='Los Angeles', parameter='pm25')
    results = body['results']
    
    #TODO: change to list comprehension
    response = []
    for result in results:

    	date = result['date']['utc']
    	value = result['value']
    	formated_result = (date, value)
    	response.append(formated_result)

    return str(response)



