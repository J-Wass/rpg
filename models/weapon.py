from effect import Effect
from item import Item
from ..constants.enums import WeaponType,weaponName
from typing import List

class Weapon(Item):
    weapon_type: WeaponType
    prefix: str

    def __init__(self,weapon_type: WeaponType, prefix:str = "", name: str = "", effects: List[Effect] = [], market_value: int = 0):
        """Initialize a new instance of an weapon object."""
        if name:
            name += " (" + prefix + " " + weaponName(weapon_type) + ")"
            super(name, effects, market_value)
        else:
            super(prefix + " " + weaponName(weapon_type), effects, market_value)
