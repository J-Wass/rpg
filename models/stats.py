class Stats:
    level : int
    xp : int

    health : int
    mana : int
    strength : int
    dexterity : int
    intelligence : int
    speed : int
    luck : int
    def __init__(self, level: int, health: int, speed: int, mana: int = 0, strength: int = 0, dexterity: int = 0, intelligence: int = 0, luck: int = 0, xp: int = 0):
        """Initialize a new Stats instance."""
        self.level = level
        self.health = health
        self.mana = mana
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.speed = speed
        self.luck = luck
        self.xp = xp
