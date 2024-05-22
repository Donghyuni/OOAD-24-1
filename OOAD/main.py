from weather import requestWeatherStatus
from fashion import FashionRecommendation
from essentials import EssentialItemRecommendation
import data_set

def display_weather():
    try:
        weather_status = requestWeatherStatus()
        for weather in weather_status:
            weather.essential_items = EssentialItemRecommendation.recommend_items(weather.weather_info)
            weather.outfit_recommendations = FashionRecommendation.recommend_outfits(["casual", "formal"])  # 카테고리는 예시
            print(weather)
        return weather_status
    except ConnectionError as e:
        print(e)

if __name__ == "__main__":
    current_weather = display_weather()
