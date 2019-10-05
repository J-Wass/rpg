from models.effect import Effect
from typing import List

class Item():
    name: str
    effects: List[Effect]
    market_value: int

    def __init__(self,name:str, effects: List[Effect] = [], market_value: int = 0):
        """Initialize a new instance of an item object."""
        self.name = name
        self.effects = effects
        self.market_value = market_value
