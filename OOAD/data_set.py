from datetime import datetime, timedelta

class dataSet:
    def __init__(self, date):
        self.date = date
        self.weather_info = None
        self.essential_items = []
        self.outfit_recommendations = []

    def __str__(self):
        return f"Date: {self.date}, Weather: {self.weather_info}, Essentials: {self.essential_items}, Outfits: {self.outfit_recommendations}"

def shortXml2DataSet(short_weather, data_set_list):
    for data in short_weather:
        for ds in data_set_list:
            ds.weather_info = data['value']  # 예시: 실제로는 더 복잡한 변환이 필요할 수 있습니다.

def middleXml2DataSet(middle_weather, data_set_list):
    for data in middle_weather:
        for ds in data_set_list:
            ds.weather_info = data['value']  # 예시: 실제로는 더 복잡한 변환이 필요할 수 있습니다.
    return data_set_list
