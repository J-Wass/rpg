from enum import Enum

class GameState(Enum):
    STARTING=0
    WORLDMAP=1
    CITY=2
    BATTLE=3
    MAINMENU=4

class ElementalType(Enum):
    NONE=0
    FIRE=1
    ICE=2
    ROCK=3
    LIGHTENING=4
    WATER=5

class StatType(Enum):
    HEALTH=0
    MANA=1
    STRENGTH=2
    INTELLIGENCE=3
    DEXTERITY=4
    SPEED=5
    LUCK=6

class ArmorType(Enum):
    RAGS=0
    PLATE_ARMOR=1
    CHAIN_MAIL=2
    ROBES=3

def armorName(armor_type: ArmorType):
    """Return the string representation of an ArmorType enum value."""
    if armor_type == ArmorType.PLATE_ARMOR:
        return "Plate Armor"
    elif armor_type == ArmorType.CHAIN_MAIL:
        return "Chain Mail"
    elif armor_type == ArmorType.ROBES:
        return "Robes"
    elif armor_type == ArmorType.RAGS:
        return "Rags"
    else:
         raise ValueError

class WeaponType(Enum):
    FISTS=0
    SWORD=1
    HALBERD=2
    LONGBOW=3
    CROSSBOW=4
    STAFF=5

def weaponName(weapon_type: WeaponType):
    """Return the string representation of an WeaponType enum value."""
    if weapon_type == WeaponType.SWORD:
        return "Sword"
    elif weapon_type == WeaponType.HALBERD:
        return "Halberd"
    elif weapon_type == WeaponType.LONGBOW:
        return "Longbow"
    elif weapon_type == WeaponType.CROSSBOW:
        return "Crossbow"
    elif weapon_type == WeaponType.STAFF:
        return "Staff"
    elif weapon_type == WeaponType.FISTS:
        return "Fists"
    else:
         raise ValueError
