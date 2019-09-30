from move import Move
from effect import Effect
from stats import Stats
from armor import Armor
from weapon import Weapon
from typing import List

class Fighter:
    name: str
    moves: List[Move]
    effects: List[Effect]
    stats: Stats
    armor: Armor
    weapon: Weapon

    def __init__(self, name: str, stats: Stats,  armor: Armor, weapon: Weapon, moves: List[Move] = [], effects: List[Effect] = []):
        """Initialize an instance of a Figher."""
        self.name = name
        self.moves = moves
        self.effects = effects
        self.stats = stats
        self.armor = armor
        self.weapon = weapon
