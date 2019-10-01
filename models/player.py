from ..models.fighter import Fighter
from ..models.item import Item
from stats import Stats
from armor import Armor
from weapon import Weapon
from ..constants.enums import ArmorType, WeaponType, weaponName, armorName
from ..constants import lists

from typing import List, Tuple
import random

class Player:
    fighter: Fighter
    location = Tuple[int,int]
    gold: int
    items: List[Item]

    def __init__(self, name: str, location: Tuple[int,int] = (0,0), gold: int = 0, items: List[Item] = []):
        """Initialize an instance of the playable character."""
        player_weapon: Weapon = Weapon(WeaponType.FISTS,self.get_random_fists_prefiz())
        player_weapon: Armor = Armor(ArmorType.RAGS,self.get_random_rags_prefix())
        player_weapon: Stats = Stats(level=1,health=100,speed=1)
        self.fighter = Fighter(name, player_weapon, player_weapon, player_weapon)
        self.location = location
        self.gold = gold
        self.items = items

    @staticmethod
    def get_random_fist_prefix():
        """Get a random prefix for fist weapon."""
        return random.choice(lists.fist_prefixes)

    @staticmethod
    def  get_random_rags_prefix():
        """Get a random prefix for rags armor."""
        return random.choice(lists.rags_prefixes)
