import urllib3
import json

def lambda_handler(event, context):
    city = event['location']['city'].lower()
    state = event['location']['state'].lower()
    try:
        country = event['location']['country'].upper()
    except:
        country = 'uk'
    
    http = urllib3.PoolManager()
    url = f"https://weather.talkpython.fm/api/weather?city={city}&state={state}&country={country}&units=imperial"
    resp = http.request('GET', url)
    data = resp.data
    
    # data = json.loads(resp.data.decode('UTF-8'))
    # Use above if getting data type error.
    
    response_object = {}
    response_object['statuscode'] = 200
    response_object['body'] = json.loads(data) #dictionary

    return response_object
    