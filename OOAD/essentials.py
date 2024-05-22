class EssentialItemRecommendation:
    @staticmethod
    def recommend_items(weather_info):
        essential_items = []
        if weather_info == "Rain":
            essential_items.append("Umbrella")
        elif weather_info == "Sunny":
            essential_items.append("Sunglasses")
        # 추가 날씨 조건 및 추천 사항 추가 가능
        return essential_items
