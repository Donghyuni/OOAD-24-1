
from weather import requestWeatherStatus
from essentials import EssentialItemContext, RainyStrategy, SunnyStrategy
from fashion import FashionContext, CasualOutfitStrategy, FormalOutfitStrategy

def display_weather():
    try:
        weather_status = requestWeatherStatus()
        for weather in weather_status:
            # Set strategies based on weather condition
            if weather.condition == "Rain":
                essential_context = EssentialItemContext(RainyStrategy())
            else:
                essential_context = EssentialItemContext(SunnyStrategy())

            weather.essential_items = essential_context.recommend_items(weather.condition)

            # Set fashion context
            fashion_context = FashionContext(CasualOutfitStrategy())
            weather.outfit_recommendations = fashion_context.recommend_outfits(["casual", "formal"])  # 카테고리는 예시
            
            print(weather)
        return weather_status
    except ConnectionError as e:
        print(e)

if __name__ == "__main__":
    current_weather = display_weather()
