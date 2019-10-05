from models.effect import Effect
from constants.enums import ElementalType

from typing import List

class Move:
    base_damage: int
    critical_chance: float
    move_speed: int
    mana_cost: int
    elemental_type: ElementalType
    range: int
    effects: List[Effect]

    def __init__(self, base_damage: int = 1.00, critical_chance: float = 0.05, move_speed: int = 1, mana_cost: int = 0, elemental_type: ElementalType = ElementalType.NONE, range: int = 1, effects: List[Effect] = []):
        """Initialize a new instance of a move for use in battle."""
        self.base_damage = base_damage
        self.critical_chance = critical_chance
        self.move_speed = move_speed
        self.mana_cost = mana_cost
        self.elemental_type = elemental_type
        self.range = range
        self.effects = effects
