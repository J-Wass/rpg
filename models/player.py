from ..models.fighter import Fighter
from ..models.item import Item
from stats import Stats
from armor import Armor
from weapon import Weapon
from ..constants.enums import ArmorType, WeaponType, weaponName, armorName

from typing import List, Tuple

class Player:
    fighter: Fighter
    location = Tuple[int,int]
    gold: int
    items: List[Item]

    def __init__(self, fighter: Fighter, location: Tuple[int,int] = (0,0), gold: int = 0, items: List[Item] = []):
        """Initialize an instance of the playable character."""
        self.fighter = fighter
        self.location = location
        self.gold = gold
        self.items = items

    @classmethod
    def generate_new_player(cls, name: str):
        """Generate a new player."""
        new_weapon: Weapon = Weapon(WeaponType.NONE)
        new_armor: Armor = Armor(ArmorType.NONE)
        new_stats: Stats = Stats(level=1,health=100,speed=1)
        new_fighter: Fighter = Fighter(name, new_stats, new_armor, new_weapon)
        return cls(fighter=new_fighter,location=(0,0))
