from models.effect import Effect
from models.item import Item
from constants.enums import ArmorType, armorName

from typing import List

class Armor(Item):
    armor_type: ArmorType
    prefix: str

    def __init__(self,armor_type: ArmorType, prefix:str, name: str = "", effects: List[Effect] = [], market_value: int = 0):
        """Initialize a new instance of an armor object."""
        if name:
            name += " (" + prefix + " " + armorName(armor_type) + ")"
            super(name, effects, market_value)
        else:
            super(prefix + " " + armorName(armor_type), effects, market_value)
