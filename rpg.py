from models.player import Player
from constants.enums import GameState
from utils import askWithOptions, askInput, newGameOrLoad, printWorldMap

import random

player: Player
game_state: int = GameState.STARTING

while True:
    if game_state == GameState.STARTING:
        player = newGameOrLoad()
        game_state = GameState.WORLDMAP
    elif game_state == GameState.WORLDMAP:
        printWorldMap(player.location)
        direction: str = askWithOptions(["North", "South", "East", "West"])
        player.location[1] += int(random.choice(range(3,7))*player.fighter.stats.speed)
