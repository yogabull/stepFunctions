# App to get weather 
import collections
import requests

Location = collections.namedtuple('Location', 'city state country')
Weather = collections.namedtuple('Weather', 'location units temp condition')

def main():
    show_header()

    # get location request
    location_text = input('Where do you want the weaterh report (e.g. Portland, State, US)? ')

    # Convert plaintext into data we can use.
    loc = convert_plaintext_location(location_text)

    # Get report from API.
    weather = call_weather_api(loc)

    # Report weather.
    print(weather)
   
def show_header():
    print('-------------------------')
    print('    Weather Client')
    print('-------------------------')
    print()

def convert_plaintext_location(location):
    if not location or not location.strip():
        return None

    parts = location.lower().strip()  
    parts = location.split(',')
    state = ''
    country = 'us'

    if len(parts) == 1:
        city = parts[0].strip()
    elif len(parts) == 2:
        city = parts[0].strip()
        state = parts[1].strip()
    elif len(parts) == 3:
        city = parts[0].lower().strip()
        state = parts[1].lower().strip()
        country = parts[2].lower().strip()
    else:
        return None

    # method1, passing a tuple.
    # loc = city, state, country
    
    # method2 - Named tuple (from the collection module)
    # passing a collection instead so the keys are known/matched with a value.
    # it is easier to program against because you can call 'state' as a method instead of an index.
    # loc2 = Location(city, state, country)

    return Location(city, state, country)

def call_weather_api(loc):

    API_key = 'e9197c13b7585232a4df7c5ee23ce56c'
    # url = "http://api.openweathermap.org/geo/1.0/direct?q={loc.city},{loc.state},{loc.country}&limit={limit}&appid={API_key}"

    # url = "http://api.openweathermap.org/geo/1.0/direct?q=dallas&limit=1&appid={api-key}"


    url = f'https://weather.talkpython.fm/api/weather?city={loc.city}&{loc.state}=US&units=imperial'
    if loc.state:
        url += f"&state={loc.state}"
    

    response = requests.get(url)
    if response.status_code in {400, 404, 500}:
        print(f"Error: {response.text}.")
        return None
    
    data = response.json()
    
    print(loc)
    print(data)

    # return convert_api_to_weather(loc, data)

def convert_api_to_weather(loc, data):
    temp = data.get('forecast').get('temp')
    w = data.get('weather')
    condition = f"{w.get('category')}: {w.get('description').capitalize()}"

    weather = Weather(loc, 'imperial', temp, condition)

    return weather


     



if __name__ == "__main__":
    main()

'''
python bytes api
https://weather.talkpython.fm/?city=Dallas&state=tx


    # print(response.status_code)
    # print(response.text)
    # print(type(response.text))
    # print()
    # # this method converts the json response to a dict.
    # print(response.json())
    # print(type(response.json()))
    # https://openweathermap.org/
'''