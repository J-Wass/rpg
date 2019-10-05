from models.player import Player
from constants.art import worldmap

from typing import Set, List
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

def askWithOptions(options: Set[str]) -> int:
    """Ask input from user with the list of options. Supports tab completion."""
    print("\n\n-------------")
    print("Start typing and use the tab key to autocomplete....\n")
    prompt: str = "Options:\n"
    for option in options:
        prompt += "-{0}\n".format(option)

    readline.parse_and_bind('tab: complete')
    readline.set_completer(SimpleCompleter(options).complete)

    choice: str = ""
    while(choice.lower() not in list(map(lambda x: x.lower(), options))):
        print(prompt)
        choice = askInput()
        print("\n")
    return choice

def askInput() -> str:
    """Ask the user for input."""
    return input("> ")

def newGameOrLoad():
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
        print("Choose a save file:")
        save_file: str = askWithOptions(saves)
        try:
            return pickle.load(saves_path + "/" + save_file)
        except:
            print("Couldn't load {0}. Make sure the file hasn't been corrupted!".format(save_file))

def printWorldMap(location: List[int]):
    """Print the worldmap with the player at the intended location."""
    x: int = int(location[0]/10)
    y: int = int(location[1]/10)

    map: List[str] = worldmap.copy()
    row: List[str] = list(map[y])
    row[x] = 'P'
    map[y] = "".join(row)

    print("\n".join(map))
    print("Location: {0},{1}".format(location[0],location[1]))