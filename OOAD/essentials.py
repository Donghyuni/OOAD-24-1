
class EssentialItemStrategy:
    def recommend(self, weather_info):
        pass

class RainyStrategy(EssentialItemStrategy):
    def recommend(self, weather_info):
        return ["Umbrella"] if weather_info == "Rain" else []

class SunnyStrategy(EssentialItemStrategy):
    def recommend(self, weather_info):
        return ["Sunglasses"] if weather_info == "Sunny" else []

class EssentialItemContext:
    def __init__(self, strategy: EssentialItemStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: EssentialItemStrategy):
        self._strategy = strategy

    def recommend_items(self, weather_info):
        return self._strategy.recommend(weather_info)

# Example usage:
# context = EssentialItemContext(RainyStrategy())
# recommendations = context.recommend_items("Rain")
# print(recommendations)
