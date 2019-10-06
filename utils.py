from models.player import Player
from constants.art import worldmap
from constants.lists import impassable_spaces

from typing import Set, List, Optional
try:
    import pyreadline
    os_type: str = "windows"
    print("Starting rpg in windows mode.")
except ImportError:
    os_type: str = "linux"
    print("Starting rpg in linux mode.")
import readline
from os import listdir, getcwd, mkdir
from os.path import isfile, join, exists
import sys
import pickle

class SimpleCompleter:
    def __init__(self, options: Set[str]):
        """Initialize a new instance of simple completer."""
        self.options = sorted(list(map(lambda x: x.lower(), options)))
        return
    def complete(self, text: str, state: int) -> str:
        """Return the state'th option from completer."""
        response: str = None
        if state == 0:
            if text:
                self.matches = [s for s in self.options
                                if s and s.startswith(text.lower())]
            else:
                self.matches = self.options[:]
        try:
            response = self.matches[state]
        except IndexError:
            response = None
        return response

def askWithOptions(options: Set[str]) -> str:
    """Ask input from user with the list of options. Supports tab completion."""
    print("-------------")
    print("Start typing and use the tab key to autocomplete....\n")
    prompt: str = "Options:\n"
    for option in options:
        prompt += "  *{0}\n".format(option)

    readline.parse_and_bind('tab: complete')
    readline.set_completer(SimpleCompleter(options).complete)

    choice: str = ""
    while(choice not in list(map(lambda x: x.lower(), options))):
        print(prompt)
        choice = askInput()
        print("\n")
    return choice

def askInput() -> str:
    """Ask the user for input."""
    user_input = input("> ").lower()
    print("\n")
    return user_input

def newGameOrLoad() -> Optional[Player]:
    """Asks the user to load or start new game."""
    start_option:str  = askWithOptions(["Start New Game", "Load Saved Game"])
    if start_option == "start new game":
        # Create a new player.
        print("Choose a name...")
        name: str = askInput()
        return Player(name)
    else:
        # Load player.
        saves_path: str = getcwd() + "\\saves"
        if not exists(saves_path):
            mkdir(saves_path)
        saves = [f for f in listdir(saves_path) if isfile(join(saves_path, f))]
        saves.append("Go Back")
        print("Choose a save file:")
        save_file: str = askWithOptions(saves)
        if save_file == "go back":
            return None
        try:
            return pickle.load(open(saves_path + "/" + save_file, "rb+"))
        except TypeError as e:
            print(str(e))
            print("Couldn't load {0}. Make sure the file hasn't been corrupted!\n".format(save_file))
            return None

def printWorldMap(location: List[int]):
    """Print the worldmap with the player at the intended location."""
    x: int = location[0]
    y: int = location[1]

    # Place the player icon 'P' in the correct spot.
    map: List[str] = worldmap.copy()
    row: List[str] = list(map[y])
    row[x] = 'P'
    map[y] = "".join(row)

    print("\n".join(map))

def canMoveTo(x: int, y: int) -> bool:
    """Determine if x,y location is traversable."""
    return worldmap[y][x] not in impassable_spaces

def presentMainMenu(player: Player):
    """Show the main menu and ask the user to select an option."""
    choice: str = askWithOptions(['Save','Stats', 'Items', 'Go Back'])
    if choice == 'save':
        print("Are you sure you want to overwrite the save at '{0}'?".format(player.fighter.name))
        confirm: str = askWithOptions(['Yes', 'No'])
        if confirm == "yes":
            saves_path: str = getcwd() + "\\saves\\" + player.fighter.name
            with open(saves_path, "wb+") as f:
                pickle.dump(player, f)
            print("Game Saved.\n")
    elif choice == 'stats':
        ## TODO:
        print("todo")
    elif choice == 'items':
        ## TODO:
        print("todo")
    else:
        ## TODO: 
        print("todo")
