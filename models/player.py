from models.fighter import Fighter
from models.item import Item
from models.stats import Stats
from models.armor import Armor
from models.weapon import Weapon
from constants.enums import ArmorType, WeaponType, GameState
from constants import lists

from typing import List
import random

class Player:
    fighter: Fighter
    location: List[int]
    gold: int
    items: List[Item]
    game_state: GameState

    def __init__(self, name: str, location: List[int] = [56,10], gold: int = 0, items: List[Item] = []):
        """Initialize an instance of the playable character."""
        player_weapon: Weapon = Weapon(weapon_type=WeaponType.FISTS,prefix=self.get_random_fists_prefix())
        player_armor: Armor = Armor(armor_type=ArmorType.RAGS,prefix=self.get_random_rags_prefix())
        player_stats: Stats = Stats(level=1,health=100,speed=1)
        self.fighter = Fighter(name=name, weapon=player_weapon, armor=player_armor, stats=player_stats)
        self.location = location
        self.gold = gold
        self.items = items
        self.game_state = GameState.WORLDMAP

    @staticmethod
    def get_random_fists_prefix():
        """Get a random prefix for fist weapon."""
        return random.choice(lists.fist_prefixes)

    @staticmethod
    def  get_random_rags_prefix():
        """Get a random prefix for rags armor."""
        return random.choice(lists.rags_prefixes)
