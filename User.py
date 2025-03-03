import random
import requests

zipcode_data = {85308: "Glendale", 85304: "Glendale", 86001: "Flagstaff", 85246: "Chandler", 85249: "Chandler"}

#------------------------------------------------------
API_KEY = "6f2c058481cdb5ad5045b5054d29987a"
URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(zipcode):
    params = {'zip': zipcode, 'appid': API_KEY}
    response = requests.get(URL, params=params)
    return response.json()

def humidity(zipcode):
    weather = get_weather(zipcode)
    humidity = weather['main']['humidity']
    return humidity

def wind_speed(zipcode):
    weather = get_weather(zipcode)
    wind_speed = weather['wind']['speed']
    return wind_speed

def temperature(zipcode):
    weather = get_weather(zipcode)
    temperature = weather['main']['temp']
    return temperature
#------------------------------------------------------


class User:
    
    def __init__(self, username, email, password, zipcode):
        self.username = username
        self.email = email
        self.password = password
        self.zipcode = zipcode

        self.total_eco_points = 0
        self.total_clothes_dried = 0

        self.humidity = humidity(int(zipcode))
        print(self.humidity)
        self.wind_speed = wind_speed(int(zipcode))
        print(self.wind_speed)
        self.temperature = temperature(int(zipcode))
        print(self.temperature)
        

#-------------------------------------
    def get_humidity(self):
        return self.humidity
    
    def set_humidity(self, humidity):
        self.humidity = humidity
    
    def update_humidity(self):
        self.humidity = humidity(self.zipcode)
        

#-------------------------------------


    def get_wind_speed(self):
        return self.wind_speed
    
    def set_wind_speed(self, wind_speed):
        self.wind_speed = wind_speed

    def update_wind_speed(self):
        self.wind_speed = wind_speed(self.zipcode)

#-------------------------------------        

    def get_temperature(self):
        return int(self.temperature)
    
    def set_temperature(self, temperature):
        self.temperature = temperature
    
    def update_temperature(self):
        self.temperature = temperature(self.zipcode)
#-------------------------------------
    def get_username(self):
        return self.username
    
    def set_username(self, username):
        self.username = username
#-------------------------------------
    
    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email

#-------------------------------------
    def get_password(self):
        return self.password
    
    def set_password(self, password):
        self.password = password


#-------------------------------------
    
    def get_zipcode(self):
        return self.zipcode
    
    def set_zipcode(self, zipcode):
        self.zipcode = zipcode

#-------------------------------------

    def get_eco_points(self):
        return int(self.total_eco_points)
    
    def set_eco_points(self, eco_points):
        self.total_eco_points = eco_points

#-------------------------------------

    def get_clothes_dried(self):
        return self.total_clothes_dried
    
    def increment_clothes_dried(self, clothes_dried):
        self.total_clothes_dried += clothes_dried

#-------------------------------------

    def calculate_time(self):
        hmax = 0.003878054* (1.067798523)**(self.temperature - 273.15)
        gs = ((25+19*self.wind_speed)*(1-(self.humidity/100))*hmax*60)/2
        time = 800/gs
        return int(time)
    def calculate_energy_saved_instance(self,x):
        energy_saved = 5*(x/30)
        return int(energy_saved)
    
    def calculate_energy_saved(self):
        energy_saved = 5*(self.total_clothes_dried/30)
        return int(energy_saved)
    
    def increment_eco_points(self):
        self.total_eco_points = 2.25*(self.total_clothes_dried/30)

    def user_city(self):
        return zipcode_data[int(self.zipcode)]
    

