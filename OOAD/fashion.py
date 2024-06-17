
class OutfitStrategy:
    def recommend(self, categories):
        pass

class CasualOutfitStrategy(OutfitStrategy):
    def recommend(self, categories):
        return ["Casual Outfit: T-shirt and Jeans"] if "casual" in categories else []

class FormalOutfitStrategy(OutfitStrategy):
    def recommend(self, categories):
        return ["Formal Outfit: Suit and Tie"] if "formal" in categories else []

class FashionContext:
    def __init__(self, strategy: OutfitStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: OutfitStrategy):
        self._strategy = strategy

    def recommend_outfits(self, categories):
        return self._strategy.recommend(categories)

# Example usage:
# context = FashionContext(CasualOutfitStrategy())
# recommendations = context.recommend_outfits(["casual", "sport"])
# print(recommendations)
