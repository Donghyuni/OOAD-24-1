class FashionRecommendation:
    @staticmethod
    def recommend_outfits(categories):
        # 임의의 코디 추천 예시
        outfit_combinations = []
        for category in categories:
            if category == "casual":
                outfit_combinations.append("Casual Outfit: T-shirt and Jeans")
            elif category == "formal":
                outfit_combinations.append("Formal Outfit: Suit and Tie")
            # 추가 카테고리 및 추천 사항 추가 가능
        return outfit_combinations
