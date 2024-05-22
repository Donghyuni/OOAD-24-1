import requests
from datetime import datetime
import xml.etree.ElementTree as ET
import data_set

class Weather:
    def __init__(self, temperature, condition, other_data):
        self.temperature = temperature
        self.condition = condition
        self.other_data = other_data

class WeatherAPI:
    API_KEY = 'hJUMsS54Qy2VDLEueMMtIA'
    BASE_URL = 'https://apihub.kma.go.kr/api/typ01/url/kma_sfctm2.php'
    
    @staticmethod
    def get_weather_data():
        current_date = datetime.now().strftime('%Y%m%d%H%M')
        params = {
            'tm': current_date,
            'stn': '0',
            'help': '1',
            'authKey': WeatherAPI.API_KEY
        }
        response = requests.get(WeatherAPI.BASE_URL, params=params)
        if response.status_code == 200:
            tree = ET.fromstring(response.content)
            items = tree.findall('.//item')
            weather_data = [{'category': item.find('category').text, 'value': item.find('fcstValue').text} for item in items]
            return weather_data
        else:
            raise ConnectionError("Failed to connect to the weather API")

def requestWeatherStatus() -> list[data_set.dataSet]:
    shortWeather = WeatherAPI.get_weather_data()
    middleWeather = WeatherAPI.get_weather_data()  # For example purpose, we call the same method. Update if different endpoint
    current_date = datetime.now()
    dataSet = [data_set.dataSet((current_date + timedelta(days=i)).strftime('%Y-%m-%d')) for i in range(8)]
    data_set.shortXml2DataSet(shortWeather, dataSet)
    dataSet = data_set.middleXml2DataSet(middleWeather, dataSet)
    for i in dataSet:
        print(str(i))
    return dataSet
