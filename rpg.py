from models.player import Player
from constants.enums import GameState
from utils import askWithOptions, newGameOrLoad, printWorldMap, canMoveTo, presentMainMenu

player: Player
game_state: int = GameState.STARTING

while True:
    if game_state == GameState.STARTING:
        player = newGameOrLoad()
        if player:
            game_state = GameState.WORLDMAP
    elif game_state == GameState.WORLDMAP:
        printWorldMap(player.location)
        direction: str = askWithOptions(["North", "South", "East", "West", "Menu"])
        if direction == "menu":
            game_state = GameState.MAINMENU
        elif direction == "north":
            if canMoveTo(player.location[0],player.location[1]-1):
                player.location[1] -= 1
        elif direction == "east":
            if canMoveTo(player.location[0]+1,player.location[1]):
                player.location[0] += 1
        elif direction == "west":
            if canMoveTo(player.location[0]-1,player.location[1]):
                player.location[0] -=  1
        else:
            if canMoveTo(player.location[0],player.location[1]+1):
                player.location[1] += 1
    elif game_state == GameState.MAINMENU:
        presentMainMenu(player)
        game_state = GameState.WORLDMAP
