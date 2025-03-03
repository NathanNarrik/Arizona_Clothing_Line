
#function to calculate the time of drying clothes using three parameters

class Saver:
    def __init__(self, wind_speed, humidity, temperature):
        self.wind_speed = wind_speed
        self.humidity = humidity
        self.temperature = temperature

    def calculate_time(self):
        time = (self.humidity * self.wind_speed) / self.temperature
        return time


def calculate_time(wind_speed, humidity, temperature):
    #calculate the time of drying clothes using three parameters
    time = (humidity*wind_speed) / temperature
    return time



