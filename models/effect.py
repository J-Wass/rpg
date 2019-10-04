from constants.enums import StatType

class Effect:
    name: str
    target_stat: StatType
    percent_modifier: float
    constant_modifier: int

    def __init__(self, name:str, target_stat: StatType, percent_modifier: float = 0.00, contant_modifier: int = 0):
        """Initialize a new effect instance."""
        self.target_stat = target_stat
        self.percent_modifier = percent_modifier
        self.name = name
