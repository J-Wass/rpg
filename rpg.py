from models.player import Player
from constants.enums import GameState
from utils import askWithOptions, newGameOrLoad, printWorldMap, canMoveTo, presentMainMenu

player: Player

while True:
    player = newGameOrLoad()
    if player:
        break

while True:
    if player.game_state == GameState.WORLDMAP:
        printWorldMap(player.location)
        direction: str = askWithOptions(["North", "South", "East", "West", "Menu"])
        if direction == "menu":
            player.game_state = GameState.MAINMENU
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
    elif player.game_state == GameState.MAINMENU:
        presentMainMenu(player)
        player.game_state = GameState.WORLDMAP
