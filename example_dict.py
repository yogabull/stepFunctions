def main():
    d = {
        'city': 'Portland',
        'state': "ME",
        'details': ['Cold', 'Snowy', 'Winter']
    }

    # print(d.get('coutnry', 'USA'))
    # d['country'] = 'AU'
    # print(d.get('coutnry', 'USA'))
    # print(d)


w = {
    "weather": {
        "description": "few clouds",
        "category": "Clouds"
    },
    "wind": {
        "speed": 5.75,
        "deg": 210
    },
    "units": "imperial",
    "forecast": {
        "temp": 50.83,
        "feels_like": 47.5,
        "pressure": 1018,
        "humidity": 40,
        "low": 41,
        "high": 57
    },
    "location": {
        "city": "Dallas",
        "state": "TX",
        "country": "US"
    },
    "rate_limiting": {
        "unique_lookups_remaining": 49,
        "lookup_reset_window": "1 hour"
    }
}

# print(w['forecast'] ['temp'])

print(w.get('forecast'))
print(w.get('forecast').get('temp'))
print(w.get('location'))
print(w.get('location').get('city'))
print(w.get('toast'))







    
    

if __name__ == '__main__':
    main()

