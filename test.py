import random
import requests
import pickle
#------------------------------------------------------
API_KEY = "6f2c058481cdb5ad5045b5054d29987a"
URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(zipcode):
    params = {'zip': zipcode, 'appid': API_KEY}
    response = requests.get(URL, params=params)
    return response.json()

def get_humidity(zipcode):
    weather = get_weather(zipcode)
    humidity = weather['main']['humidity']
    return humidity

def get_wind_speed(zipcode):
    weather = get_weather(zipcode)
    wind_speed = weather['wind']['speed']
    return wind_speed

def get_temperature(zipcode):
    weather = get_weather(zipcode)
    temperature = weather['main']['temp']
    return temperature
#------------------------------------------------------




from pyzipcode import ZipCodeDatabase

zipcode_data = ZipCodeDatabase()
print(zipcode_data)
def city(x):
    city = zipcode_data[x].city
    return city if city else 'None'

f = open('users.txt', 'bw')
pickle.dump(zipcode_data, f)