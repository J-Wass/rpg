from models.move import Move
from models.effect import Effect
from models.stats import Stats
from models.armor import Armor
from models.weapon import Weapon
from constants.enums import StatType

from typing import List
import random

class Fighter:
    name: str
    moves: List[Move]
    effects: List[Effect]
    stats: Stats
    armor: Armor
    weapon: Weapon
    stat_xp: List[int]

    def __init__(self, name: str, stats: Stats,  armor: Armor, weapon: Weapon, moves: List[Move] = [], effects: List[Effect] = []):
        """Initialize an instance of a Figher."""
        self.name = name
        self.moves = moves
        self.effects = effects
        self.stats = stats
        self.armor = armor
        self.weapon = weapon

    def gain_xp(self, xp:int, stat_xp: List[int] = []):
        """Increment xp points of fighter. If xp goes over the cap, triggers a level up."""
        # Gain all stat xp for each StatType.
        for x in range(len(stat_xp)):
            self.stat_xp[x] += stat_xp[x]

        # Award xp, check for level-up condition.
        self.stats.xp += xp
        if self.stats.xp > self.stats.level ** 2:
            self.level_up()

    def level_up(self):
        """Level the fighter and increases stats based off of enemies beaten."""
        # Reset and award leftover xp.
        self.stats.xp = self.stats.xp % (self.stats.level ** 2)
        self.stats.level += 1

        # Increase stats based off of what enemies were beaten.
        # Enemies that train strength for example cause strength to increment.
        total_stat_xp: int = sum(self.stat_xp)
        strength_percent = self.stat_xp[StatType.STRENGTH]/total_stat_xp
        dexterity_percent = self.stat_xp[StatType.DEXTERITY]/total_stat_xp
        intelligence_percent = self.stat_xp[StatType.INTELLIGENCE]/total_stat_xp

        old_health: int = self.stats.health
        old_mana: int = self.stats.mana
        old_strength: int = self.stats.strength
        old_dexterity: int = self.stats.dexterity
        old_intelligence: int = self.stats.intelligence
        old_speed: int = self.stats.speed

        # Stats that were trained harder have a higher chance of incrementing.
        for x in range(4):
            x = random.uniform(0.0, 1.0)
            if (x < strength_percent):
                self.stats.strength += 1
            elif (x < strength_percent + dexterity_percent):
                self.stats.dexterity += 1
            elif(x < strength_percent + dexterity_percent + intelligence_percent):
                self.stats.intelligence += 1
            else:
                self.stats.speed += 1

        self.stats.health += 10
        self.stats.mana += 2

        print("\nCongrats! You have reached level {0}!".format(self.stats.level))
        print("\nHealth:\t{0} -> {1} (+{2})".format( old_health, self.stats.health, self.stats.health-old_health))
        print("\nMana:\t{0} -> {1} (+{2})".format( old_mana, self.stats.mana, self.stats.mana-old_mana))
        print("\nStrength:\t{0} -> {1} (+{2})".format( old_strength, self.stats.strength, self.stats.strength-old_strength))
        print("\nDexterity:\t{0} -> {1} (+{2})".format( old_dexterity, self.stats.dexterity, self.stats.dexterity-old_dexterity))
        print("\nIntelligence:\t{0} -> {1} (+{2})".format( old_intelligence, self.stats.intelligence, self.stats.intelligence-old_intelligence))
        print("\nSpeed:\t{0} -> {1} (+{2})".format( old_speed, self.stats.speed, self.stats.speed-old_speed))
