import requests
import json
import style
import lib
import constants
import pickle
import numpy as np


def load_model(modelfile):
	loaded_model = pickle.load(open(modelfile, 'rb'))
	return loaded_model


# OpenWeatherMap API endpoint
url = 'http://api.openweathermap.org/data/2.5/weather?q={}'

# API key
api_key = constants.API_KEY
city_name = input("Enter city name: ")

# Format the URL with the city name and API key
request_url = url.format(city_name) + f'&appid={api_key}&units=metric'

#Send a GET request to the API and store the response
response = requests.get(request_url)


#Function to verify request
def verify():
    if response.status_code == 200:
        return True
    else:
        return False


if verify():
    data = json.loads(response.text)
    TEMP=data['main']['temp']
    MIN_TMEP=data['main']['temp_min']
    MAX_TEMP=data['main']['temp_max']
    HUMIDITY=data['main']['humidity']
    DESC=data['weather'][0]['description']
    style.heading()
    style.city(city_name)
    style.temperature(int(TEMP))
    
    print(f"{'Minimum Temperature: ': <22}{MIN_TMEP}")
    print(f"{'Maximum Temperature: ': <22}{MAX_TEMP}")
    print(f"{'Humidity: ': <22}{HUMIDITY}")
    print(f"{'Description: ': <22}{DESC}")
    # feature_list=[56, 32, 33, TEMP, HUMIDITY, 5.5, 153]
    # single_pred = np.array(feature_list).reshape(1,-1)
    # loaded_model = load_model('model.pkl')
    # prediction = loaded_model.predict(single_pred)
    # print(f"{'Recomended Crop: ': <22}{prediction.item().title()}")
else:
    print('City name is Invalid!')


    
