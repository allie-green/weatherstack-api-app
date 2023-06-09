import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

service = 'http://api.weatherstack.com/forecast'
api_key = os.getenv('API_KEY')

while True:
    print('\nEnter location, or press ENTER to exit.')
    in_location = input('Location: ')
    if not in_location or in_location.isspace() : 
        print('Thank you for using the weather app. Have a great day!')
        break

    params = {
        "access_key" : api_key,
        "query": in_location,
    }

    try:
        response = requests.get(service, params)
        response.raise_for_status()
        data = json.loads(response.text)

        if data.get("success") is False:
            info = data["error"]["info"]
            code = data["error"]["code"]
            type_description = data["error"]["type"].replace("_", " ").capitalize()
            print(f'\n{info}\nError code: {code}. {type_description}.\n')
            break

        name = data["location"]["name"] 
        region = data["location"]["region"]
        country = data["location"]["country"]
        temperature = data["current"]["temperature"]
        wind = data["current"]["wind_speed"]
        description = data["current"]["weather_descriptions"][0]

        if name == region:
            weather = f'\nThe weather in {name}, {country} is {description.lower()}.\nThe temperature is {temperature} degrees Celsius, with wind speeds of {wind} km/h.'
        else: 
            weather = f'\nThe weather in {name}, {region}, {country} is {description.lower()}.\nThe temperature is {temperature} degrees Celsius, with wind speeds of {wind} km/h.'
        
        print(weather)
        
    except (requests.exceptions.RequestException, ValueError) as error:
        print(f'\nAn error occurred: {str(error)}\n')
        continue