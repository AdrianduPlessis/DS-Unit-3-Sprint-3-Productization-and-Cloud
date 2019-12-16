import openaq
api = openaq.OpenAQ()

def get_latest_observations(city='Los Angeles', parameter='pm25'):
    status, body = api.measurements(city=city, parameter=parameter)
    results = body['results']
    
    #TODO: change to list comprehension
    response = []
    for result in results:
        date = result['date']['utc']
        value = result['value']
        formated_result = (date, value)
        response.append(formated_result)

    return response