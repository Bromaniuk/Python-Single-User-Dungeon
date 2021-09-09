# import doctest
import itertools
import random
import time
import ascii_art


# ------- Color codes for text ------
def RED() -> str:
    """Create a string that signifies the terminal color red escape character.

    :return: a string
    """
    return '\033[31m'


def GREEN() -> str:
    """Create a string that signifies the terminal color green escape character.

    :return: a string
    """
    return '\033[32m'


def YELLOW() -> str:
    """Create a string that signifies the terminal color yellow escape character.

    :return: a string
    """
    return '\033[33m'


def BLUE() -> str:
    """Create a string that signifies the terminal color blue escape character.

    :return: a string
    """
    return '\033[34m'


def END_COLOR() -> str:
    """Create a string that signifies the end of a terminal color escape character.

    :return: a string
    """
    return '\033[0m'


# ------ Constants -----
def MIN_FLEE_DMG():
    """Create a value for the minimum damage that can be inflicted when fleeing.

    :return: an integer
    """
    return 1


def MAX_FLEE_DMG():
    """Create a value for the minimum damage that can be inflicted when fleeing.

    :return: an integer
    """
    return 4


def BOSS_LOCATION() -> tuple:
    """Create a tuple that assigns the game boss coordinates (x,y).

    :return: a tuple
    """
    return 20, 20


def BOSS_MAX_HEALTH():
    """Create a value representing the boss' maximum health.

    :return: an integer
    """
    return 50


def BOSS_MAX_DAMAGE() -> int:
    """Create a Maximum value that represents a boss characters maximum damage.

    :return: an integer
    """
    return 15


def CLASS_NERD_MAX_HEALTH() -> tuple:
    """Create a tuple that contains values corresponding to maximum health per character level.

    :return: a tuple
    """
    return 14, 18, 24


def CLASS_NERD_MAX_DAMAGE() -> tuple:
    """Create a tuple that contains values corresponding to maximum damage per character level.

    :return: a tuple
    """
    return 14, 18, 24


def CLASS_NERD_EXP_LVL() -> tuple:
    """Create a tuple that contains values corresponding to minimum exp to level up, per level.

    :return: a tuple
    """
    return 50, 150, 'MAX'


def CLASS_JOCK_MAX_HEALTH() -> tuple:
    """Create a tuple that contains values corresponding to maximum health per character level.

    :return: a tuple
    """
    return 22, 27, 32


def CLASS_JOCK_MAX_DAMAGE() -> tuple:
    """Create a tuple that contains values corresponding to maximum damage per character level.

    :return: a tuple
    """
    return 22, 27, 32


def CLASS_JOCK_EXP_LVL() -> tuple:
    """Create a tuple that contains values corresponding to minimum exp to level up, per level.

    :return: a tuple
    """
    return 150, 300, 'MAX'


def CLASS_PRETTYGIRL_MAX_HEALTH() -> tuple:
    """Create a tuple that contains values corresponding to maximum health per character level.

    :return: a tuple
    """
    return 17, 22, 27


def CLASS_PRETTYGIRL_MAX_DAMAGE() -> tuple:
    """Create a tuple that contains values corresponding to maximum damage per character level.

    :return: a tuple
    """
    return 17, 22, 27


def CLASS_PRETTYGIRL_EXP_LVL() -> tuple:
    """Create a tuple that contains values corresponding to minimum exp to level up, per level.

    :return: a tuple
    """
    return 100, 200, 'MAX'


def CLASS_GOTHKID_MAX_HEALTH() -> tuple:
    """Create a tuple that contains values corresponding to maximum health per character level.

    :return: a tuple
    """
    return 12, 32, 52


def CLASS_GOTHKID_MAX_DAMAGE() -> tuple:
    """Create a tuple that contains values corresponding to maximum damage per character level.

    :return: a tuple
    """
    return 12, 27, 42


def CLASS_GOTHKID_EXP_LVL() -> tuple:
    """Create a tuple that contains values corresponding to minimum exp to level up, per level.

    :return: a tuple
    """
    return 50, 200, 'MAX'


def LUNCH_LADY_MAX_HEALTH() -> int:
    """Create a value representing a foes maximum health.

    :return: an integer
    """
    return 10


def LUNCH_LADY_MAX_DAMAGE() -> int:
    """Create a value representing a foes maximum damage.

    :return: an integer
    """
    return 10


def TEACHER_MAX_HEALTH() -> int:
    """Create a value representing a foes maximum health.

    :return: an integer
    """
    return 15


def TEACHER_MAX_DAMAGE() -> int:
    """Create a value representing a foes maximum damage.

    :return: an integer
    """
    return 10


def JANITOR_MAX_HEALTH() -> int:
    """Create a value representing a foes maximum health.

    :return: an integer
    """
    return 20


def JANITOR_MAX_DAMAGE() -> int:
    """Create a value representing a foes maximum damage.

    :return: an integer
    """
    return 10


def CLASS_CLOWN_MAX_HEALTH() -> int:
    """Create a value representing a foes maximum health.

    :return: an integer
    """
    return 10


def CLASS_CLOWN_MAX_DAMAGE() -> int:
    """Create a value representing a foes maximum damage.

    :return: an integer
    """
    return 10


def BULLY_MAX_HEALTH() -> int:
    """Create a value representing a foes maximum health.

    :return: an integer
    """
    return 12


def BULLY_MAX_DAMAGE() -> int:
    """Create a value representing a foes maximum damage.

    :return: an integer
    """
    return 10


def MEANGIRL_MAX_HEALTH() -> int:
    """Create a value representing a foes maximum health.

    :return: an integer
    """
    return 10


def MEANGIRL_MAX_DAMAGE() -> int:
    """Create a value representing a foes maximum damage.

    :return: an integer
    """
    return 10


def TEACHERSPET_MAX_HEALTH() -> int:
    """Create a value representing a foes maximum health.

    :return: an integer
    """
    return 8


def TEACHERSPET_MAX_DAMAGE() -> int:
    """Create a value representing a foes maximum damage.

    :return: an integer
    """
    return 10


def SECRETARY_MAX_HEALTH() -> int:
    """Create a value representing a foes maximum health.

    :return: an integer
    """
    return 22


def SECRETARY_MAX_DAMAGE() -> int:
    """Create a value representing a foes maximum damage.

    :return: an integer
    """
    return 11


def EXP_MULTIPLIER() -> float:
    """Create a value representing an experience multiplier applied dependant on foe health points.

    :return: a floating point number
    """
    return 1.5


def make_character() -> dict:
    """Create dictionary to represent the user's character information.

    :postcondition: initializes the first instance of the character dictionary
    :return: a dictionary with keys: name, current_coordinates, level, exp, location, inventory

    """
    print("Another boring day at Riverside High School...")
    time.sleep(2)
    intro_dialogue()
    character = {"name": (input("Billy: Wait...What's your codename again?\nYou: ")).title(),
                 "current_coordinates": [0, 0], 'level': 1, 'exp': 0, 'location': 'Playground',
                 'inventory': [], 'class': {'name': ''}}
    get_class_choice(character)
    print(f"Bill: Alright! So {character['name']} the {character['class']['name']}, eh? Lets get crackin'!")
    time.sleep(2)
    return character


def print_with_pause(phrase):
    """Print a string followed by a brief pause.

    :param phrase: a printable data structure
    :precondition: phrase must be a printable data structure
    :postcondition: prints an object and adds time delay
    :return: none

    >>> string = "Hello World"
    >>> print_with_pause(string)
    Hello World
    >>> string = 345.2
    >>> print_with_pause(string)
    345.2
    """
    print(phrase)
    time.sleep(3)


def intro_dialogue():
    """Print a dialogue at start of game.

    :precondition: function must be called
    :postcondition: print a long dialogue including pauses combined with ascii art
    :return: none

    """
    choice = input("Enter '1' to play the introduction dialogue, enter any other key to skip to gameplay.")
    if choice == '1':
        strings = ["You are dozing in and out during Math class...", "\nMr.Thompson: ..ahem..",
                   "Mr.Thompson: Ahem.", "Mr.Thompson: !!AHEM!!", "\nYou jolt awake!",
                   "You open your eyes and see your math teacher, and everyone else in the class, staring at you!",
                   "\nMr.Thompson: Aha! I assume you are so tired because you were up all last night studying!",
                   "Mr.Thompson: In that case, please tell me what the 96th number in the fibonacci sequence is!",
                   "You: Uhhmmm... is it... ", "\nRRRRRIIIIIINNNNGGGG!",
                   "\nMr.Thompson: Hmm... It seems like you've been saved by the bell once again.",
                   "Mr.Thompson: None the matter! Report to Principal Filbert's office after school for 3 hours "
                   "of detention!", "\nRats! That was totally bogus, man!",
                   "You head outside and meet up with your group of friends...",
                   "\nBill: Hey man, that was so not cool of Mr.Thompson!",
                   "Ted: Yeah! I wish there was something we could do to get back at all of the lame teachers!",
                   "Bill: I've got it! Let's execute Operation Swordfish! Everyone got their walkie-talkies?",
                   "Ted: Yeah! Let's do it, dude! I'll head to the Cafeteria and start a food-fight! My "
                   "codename will be Hawk!", "Bill: I'll go to the Teacher's Lounge and burn popcorn in their "
                                             "microwave! You can call me Bullseye over the radio!",
                   "Billy: Dude, remember the plan? You've got to take on Principal Filbert!"]
        ascii_art.teacher()
        list(map(print_with_pause, strings))


def get_class_choice(character: dict):
    """Receive input from user based on options presented.

    Takes a users input from a list of choices and assigns the class of choice to the character dictionary

    :param character: a dictionary
    :precondition: character must be a dictionary
    :postcondition: assigns one of the choices presented as the key-value pair of the character dictionary
    :return: none
    """
    class_options = [f"{GREEN()}\033[1mNerd\033[0m - You're a Nerd. That's right. I said it. You spend most "
                     f"nights staying up late to study and play with rubik's cubes.\nYou are proud to be a "
                     f"Nerd. However, teachers have been assigning you homework that you think is beneath you "
                     f"and you are SICK of it!\nThis is your chance to fight back against the teachers you loathe!"
                     f" (EASY: Fast leveling, weak start)\n",
                     f"{BLUE()}\033[1mJock\033[0m - Is your name Chad? It probably is. You have been playing "
                     f"every sport out there since you were old enough to throw a ball.\nIt's kind of all you "
                     f"know. Like, really, you're failing most of your courses besides gym class. You are more "
                     f"than ready to fight back\nagainst the administration and this is your chance! (EASY)\n",
                     f"{YELLOW()}\033[1mPretty Girl\033[0m - You put more effort into your captions on Instagram "
                     f"than you have for this entire school year. It's time to give up.\nYou barely classify as "
                     f"a micro-influencer. You've been able to get decent grades so far since all you do is ask "
                     f"the nearest nerd\nif they would like to do your homework for you. However, your teachers "
                     f"are beginning to realize that you are cheating and are getting your parents involved.\nI "
                     f"think it's about time you gave the administration a piece of your mind! No matter "
                     f"how small it is! (MEDIUM)\n",
                     f"{RED()}\033[1mGoth Kid\033[0m - They just don't get you. We understand. But, maybe the "
                     f"tri-color mohawk is a bit much? No? Okay, that's fine.\nJust put your headphones back on, "
                     f"resume your Linkin Park playlist, and let's go to war! (HARD: Slow leveling but high gains)"]
    class_chosen = False
    while not class_chosen:
        print("\nCool Cool... So are you a...\n")
        for number, class_option in enumerate(class_options, 1):
            print(f"{number} - {class_option}")
        class_choice = input("")
        if validate_class_choice(class_choice):
            assign_class(character, class_choice)
            class_chosen = True


def validate_class_choice(class_choice: str) -> bool:
    """Assert that the user choice is one of the options and return a boolean.

    :param class_choice: a string corresponding to the list of choice integers
    :precondition: class_choice must be a string of either "1", "2", "3" or "4"
    :postcondition: returns a boolean value corresponding with the set conditional
    :return: a boolean

    >>> choice = "1"
    >>> validate_class_choice(choice)
    True
    >>> choice = "4"
    >>> validate_class_choice(choice)
    True
    >>> choice = "one"
    >>> validate_class_choice(choice)
    Sorry, that's not a valid choice! Please try again.
    False
    """
    if class_choice in ["1", "2", "3", "4"]:
        return True
    else:
        print("Sorry, that's not a valid choice! Please try again.")
        return False


def assign_class(character: dict, class_choice: str):
    """Assign a nested class dictionary to character dictionary.

    Assigns a nested dictionary based on chosen class and adds it to the character dictionary by key 'class' and assigns
    character health to respected class.

    :param character: a dictionary
    :param class_choice: a string
    :precondition: character must be a dictionary and contain at least a key-value pair of 'level':int and 'health':int
                    class_choice must be a string representing either "1", "2", "3" or "4"
    :postcondition: updates the dictionary character to contain a nested dictionary under the key 'class', and assigns
                    character key value pair 'health' based on that class value
    :return: none

    >>> char, choice = {'health': 20, 'level': 1} , "2"
    >>> assign_class(char, choice)
    >>> print(char)
    {'health': 22, 'level': 1, 'class': {'name': 'Jock', 'level_name': ('Wrestling Amateur', 'Basketball Lead', \
'Football Captain'), 'MAX_DMG': (22, 27, 32), 'MAX_HEALTH': (22, 27, 32), 'attack': 'You throw a football \
and hit the', 'EXP_REQ': (150, 300, 'MAX')}}
    """
    nerd = {'name': 'Nerd', 'level_name': ('Math Wiz', 'Computer Lab Lurker', 'Chess Club President'),
            'MAX_DMG': CLASS_NERD_MAX_DAMAGE(), 'MAX_HEALTH': CLASS_NERD_MAX_HEALTH(),
            'attack': 'You throw a calculator and hit the', 'EXP_REQ': CLASS_NERD_EXP_LVL()}
    jock = {'name': 'Jock', 'level_name': ('Wrestling Amateur', 'Basketball Lead', 'Football Captain'),
            'MAX_DMG': CLASS_JOCK_MAX_DAMAGE(), 'MAX_HEALTH': CLASS_JOCK_MAX_HEALTH(),
            'attack': 'You throw a football and hit the', 'EXP_REQ': CLASS_JOCK_EXP_LVL()}
    pretty_girl = {'name': 'Pretty Girl', 'level_name': ('Blonde Bombshell', 'Cunning Brunette', 'Seductive Redhead'),
                   'MAX_DMG': CLASS_PRETTYGIRL_MAX_DAMAGE(), 'MAX_HEALTH': CLASS_PRETTYGIRL_MAX_HEALTH(),
                   'attack': 'You throw a pumpkin spice latte and hit the', 'EXP_REQ': CLASS_PRETTYGIRL_EXP_LVL()}
    goth_kid = {'name': 'Goth Kid', 'level_name': ('Emo', 'Metalhead', 'Anarchist'),
                'MAX_DMG': CLASS_GOTHKID_MAX_DAMAGE(), 'MAX_HEALTH': CLASS_GOTHKID_MAX_HEALTH(),
                'attack': 'You throw a voodoo doll and hit the', 'EXP_REQ': CLASS_GOTHKID_EXP_LVL()}
    if class_choice == "1":
        character['class'] = nerd
        character['health'] = nerd['MAX_HEALTH'][character['level'] - 1]
    elif class_choice == "2":
        character['class'] = jock
        character['health'] = jock['MAX_HEALTH'][character['level'] - 1]
    elif class_choice == "3":
        character['class'] = pretty_girl
        character['health'] = pretty_girl['MAX_HEALTH'][character['level'] - 1]
    elif class_choice == "4":
        character['class'] = goth_kid
        character['health'] = goth_kid['MAX_HEALTH'][character['level'] - 1]


def make_board() -> dict:
    """Create a dictionary with key-value pairs that represent a game board.

    :precondition: function must be called
    :postcondition: creates a dictionary with key-value pairs "(x, y)": string
    :return: a dictionary with (x, y) keys where x and y are integers in range [0, 4]
    """
    board = {(x_value, y_value): ' \U0001F7EB ' for y_value in range(25) for x_value in range(25)}
    board[BOSS_LOCATION()] = ' \U0001F47A '
    assign_items_to_location(board)
    return board


def assign_items_to_location(board: dict):
    """Assign items at random to a location on the game board.

    :param board: a dictionary
    :precondition: board must be a dictionary containing key-value pair of (x, y) where x and y are in range 0 to 24
    :postcondition: assigns a string to the key in the board dictionary at random
    :return: none
    """
    for item in range(7):
        board[(random.randint(0, 23), random.randint(0, 23))] = ' \U0001F4C4 '


def location(character: dict, board: dict, notes: list):
    """Print location description with board visual.

    :param character: a dictionary representing the user's character
    :param board: a dictionary
    :param notes: a list
    :precondition: character must be a dictionary with "current_coordinates" key
    :precondition: "current_coordinates" value must be a list with two values in range [0, 4]
    :precondition: elements in the "notes" list must be strings
    :postcondition: prints a description of the user's current location on the board
    :postcondition: prints a map with character represented in correct location
    :postcondition: prints information regarding the character's current health/location/exp
    :return: None

    """
    generate_description(character)
    board_visual(character, board, notes)
    check_status(character)


def generate_description(character: dict):
    """Generate a different description of an area based on the location of the player.

    :param character: a dictionary
    :precondition: character must be a dictionary that contains the key-value pair 'location':string
    :postcondition: print a description of the area the player is currently in based on character
    dictionary key-value pair 'location'
    :return: none

    """
    verbs = ["look around", "stare in to the distance", "stumble", "trip", "pause", "take a breath", "scan the area"]
    adjectives = ["big", "small", "weird", "strange", "awkward", "young", "strong"]
    playground = ["person", "class clown", "bully", "pretty girl", "emo kid", "geek", "tomboy",
                  "band-kid", "foreign student"]
    cafeteria = ["cafeteria lady", "line cook", "bully", "pretty girl", "emo kid", "geek", "tomboy",
                 "class clown", "janitor"]
    teachers_lounge = ["substitute teacher", "teacher", "janitor", "secretary", "counsellor"]
    principals_office = ["substitute teacher", "teacher", "secretary", "counsellor", "parent", "vice-principal"]
    if character['location'] == 'Playground':
        print(f"\nYou {random.choice(verbs)} and see a {random.choice(adjectives)} "
              f"{random.choice(playground)}.")
    elif character['location'] == 'Cafeteria':
        print(f"\nYou {random.choice(verbs)} and see a {random.choice(adjectives)} "
              f"{random.choice(cafeteria)}.")
    elif character['location'] == "Teacher's Lounge":
        print(f"\nYou {random.choice(verbs)} and see a {random.choice(adjectives)}"
              f" {random.choice(teachers_lounge)}.")
    elif character['location'] == "Principal's Office":
        print(f"\nYou {random.choice(verbs)} and see a {random.choice(adjectives)}"
              f" {random.choice(principals_office)}.")


def board_visual(character: dict, board: dict, notes: list):
    """Print ASCII board visual.

    Represents the map and character's current location.

    :param character: a dictionary representing the user's character
    :param board: a dictionary representing the game board
    :param notes: a list
    :precondition: character must be a dictionary with "current_coordinates" key
    :precondition: "current_coordinates" value must be a list with two values in range [0, 4]
    :precondition: board must be a dictionary with (x, y) keys where x and y are integers in range [0, 4]
    :precondition: notes must be a list of one or more strings
    :postcondition: prints a map with character represented in correct location
    :postcondition: checks to see if there is an item at the character's location
    :return: None
    """
    if board[tuple(character['current_coordinates'])] == ' \U0001F4C4 ':
        get_item(character, notes)
    board[tuple(character['current_coordinates'])] = " \U0001F93A "
    for y_coord in range(25):
        row = ""
        for x_coord in range(25):
            row += board[(x_coord, y_coord)]
        print(row)
    board[tuple(character['current_coordinates'])] = " \U0001F7EB "


def get_item(character: dict, notes: list):
    """Add an item that you encounter on the map to your character inventory.

    :param character: a dictionary
    :param notes: a list
    :precondition: character must be a dictionary with a key-value pair 'inventory':list
    :precondition: notes must be a list containing at least 1 string
    :postcondition: print a phrase that tells the character what item they have picked up and adds that item to the
                    character dictionary under the key 'inventory' and then removes that item from source list
    :return: none

    >>> note = ["a","b","c"]
    >>> char = {'inventory': []}
    >>> get_item(char, note)
    You notice a scrap of paper on the ground with the letter 'a' written on it... Hmm... You might need this later.
    You put it in your backpack!
    """
    print(f"You notice a scrap of paper on the ground with the letter '{notes[0]}' written on it... Hmm... "
          f"You might need this later.\nYou put it in your backpack!")
    time.sleep(3)
    character['inventory'].append(notes[0])
    notes.pop(0)


def check_status(character: dict):
    """Print current information about the character's location, health, and exp.

    :param character: a dictionary
    :precondition: character must be a dictionary containing key-value pair of 'location':string, 'name':string,
                    'class':string, 'health':int, 'exp':int
    :postcondition: checks map location and prints a status containing numerous values that are stored in the character
                    dictionary
    :return: none

    """
    region(character)
    print(f"You are in the:" + f"{YELLOW()}" + f"{character['location']}" + f"{END_COLOR()}")
    print(f"{character['name']}: The level {character['level']} "
          f"{character['class']['level_name'][character['level'] - 1]}.")
    print(
        f"{RED()}" + f"HP: {character['health']}/{character['class']['MAX_HEALTH'][character['level'] - 1]}" +
        f"{END_COLOR()}" + "\t " f"{GREEN()}" +
        f"EXP: {character['exp']}/{character['class']['EXP_REQ'][character['level'] - 1]}" + f"{END_COLOR()}")


def region(character: dict):
    """Assign specific region to character dictionary dependant on coordinates.

    :param character: a dictionary
    :precondition: character must be a dictionary that contains key-value pair "current_coordinates":"(x,y) and
                    "location": string
    :postcondition: assigns character dictionary key-value pair "location" to a string corresponding to set coordinates
    :return: none

    >>> player = {'current_coordinates': [16, 15], 'location': 'Playground'}
    >>> region(player)

    >>> player
    {'current_coordinates': [16, 15], 'location': 'Cafeteria'}
    """
    if character['current_coordinates'][0] <= 15 and character['current_coordinates'][1] <= 15:
        character['location'] = "Playground"
    elif character['current_coordinates'][0] > 15 and character['current_coordinates'][1] <= 15:
        character['location'] = "Cafeteria"
    elif character['current_coordinates'][0] <= 15 and character['current_coordinates'][1] > 15:
        character['location'] = "Teacher's Lounge"
    elif character['current_coordinates'][0] > 15 and character['current_coordinates'][1] > 15:
        character['location'] = "Principal's Office"


def get_user_choice(character: dict) -> str:
    """Ask user which direction to move their character.

    :param character: a dictionary representing the user's character
    :precondition: character must be a dictionary with key-value pairs 'name':string, 'inventory':list
    :postcondition: accepts input for user's choice of direction
    :return: a string of the user's inputted direction
    """
    direction = (input(f"Which way would you like to go, {character['name']}? (Enter 'menu' "
                       f"for options) \n")).lower()
    while direction == "menu":
        menu()
        direction = (input("Now that you know your options, which way would you like to go?"))
    if direction in ["0", "quit"]:
        print("You cower in fear at the possibility of facing any real challenges while "
              "chasing your dreams in life... chicken. \n THE END")
        quit()
    while direction == '5':
        check_inventory(character)
        direction = (input("Now that you have looked in your backpack, which way would you like to go?"))
    return direction


def menu():
    """Print all valid options for user to input.

    :precondition: function must be called
    :postcondition: prints an enumerated list of options for the character's turn
    :return: None

    >>> menu()
    Enter the number corresponding to your desired choice:
    0 - Quit
    1 - Up/North
    2 - Right/East
    3 - South/Down
    4 - Left/West
    5 - Backpack
    """
    options = ["Quit", "Up/North", "Right/East", "South/Down", "Left/West", 'Backpack']
    print("Enter the number corresponding to your desired choice:")
    for number, option in enumerate(options):
        print(f"{number} - {option}")


def check_inventory(character: dict):
    """Check character inventory for a collection of items.

    :param character: a dictionary
    :precondition: character must be a dictionary that contains the key-value pair 'inventory':list
    :postcondition: print a string that contains the letters of notes you have that are stored in the dictionary
    :return: none

    >>> char =  {'inventory': ["s","t","o"]}
    >>> check_inventory(char)
    You reach into your back pack and pull out a few scraps of paper. All put together, you have the letters sto.
    >>> char = {'inventory': []}
    >>> check_inventory(char)
    You do not have anything interesting in your backpack.
    """
    if len(character['inventory']) > 0:
        print(f"You reach into your back pack and pull out a few scraps of paper. "
              f"All put together, you have the letters {list(itertools.accumulate(character['inventory']))[-1]}.")
    else:
        print("You do not have anything interesting in your backpack.")


def validate_move(character: dict, direction: str) -> bool:
    """Evaluate if character can move in desired direction.

    :param character: a dictionary representing the user's character
    :param direction: a string
    :precondition: character must be a dictionary with "current_coordinates" key
    :precondition: "current_coordinates" value must be a list with two values in range [0, 4]
    :postcondition: checks if direction is possible movement option
    :postcondition: evaluates whether the character can move in desired direction
    :return: True or False

    >>> validate_move({"current_coordinates": [0, 3]}, "1")
    True
    >>> validate_move({"current_coordinates": [5, 5]}, "2")
    True
    >>> validate_move({"current_coordinates": [24, 24]}, "4")
    True
    >>> validate_move({"current_coordinates": [24, 12]}, "2")
    False
    >>> validate_move({"current_coordinates": [8, 24]}, "3")
    False
    """
    if direction == "1" and 24 >= (character["current_coordinates"][1] - 1) >= 0:
        return True
    elif direction == "2" and 24 >= (character["current_coordinates"][0] + 1) >= 0:
        return True
    elif direction == "3" and 24 >= (character["current_coordinates"][1] + 1) >= 0:
        return True
    elif direction == "4" and 24 >= (character["current_coordinates"][0] - 1) >= 0:
        return True
    else:
        return False


def move_character(character: dict, direction: str) -> dict:
    """Move character to desired location.

    :param character: a dictionary representing the user's character
    :param direction: a string
    :precondition: character must be a dictionary with "current_coordinates" key
    :precondition: "current_coordinates" value must be a list with two values in range [0, 4]
    :precondition: direction must be in [1, 2, 3, 4]
    :postcondition: adjusts character's current coordinates to desired location
    :return: character dictionary with the current coordinates modified

    >>> move_character({"current_coordinates": [0, 3]}, "1")
    {'current_coordinates': [0, 2]}
    >>> move_character({"current_coordinates": [0, 0]}, "2")
    {'current_coordinates': [1, 0]}
    >>> move_character({"current_coordinates": [2, 0]}, "3")
    {'current_coordinates': [2, 1]}
    >>> move_character({"current_coordinates": [1, 0]}, "4")
    {'current_coordinates': [0, 0]}
    """
    if direction == "1":
        character["current_coordinates"][1] -= 1
    if direction == "2":
        character["current_coordinates"][0] += 1
    if direction == "3":
        character["current_coordinates"][1] += 1
    if direction == "4":
        character["current_coordinates"][0] -= 1
    return character


def check_for_monsters() -> bool:
    """Generate 20% chance for a monster encounter.

    :precondition: function must be called
    :postcondition: rolls for monster encounter with a 20% chance to encounter
    :return: a boolean
    """
    return True if random.randint(1, 100) <= 20 else False


def fight_or_flight(character: dict):
    """Ask user if they want to fight monster encounter or flee.

    :param character: a dictionary representing the user's character
    :precondition: character must be a dictionary with "health" key
    :precondition: "health" value must be an integer
    :postcondition: correctly modifies character's health value if necessary
    :return: character dictionary possibly with modified health value
    """
    foe = foe_region_generator(character)
    decision = input(f"\nLook out! A {foe['name']}! \n Would you like to risk detention and "
                     "engage in educational warfare? (Enter '1' to fight or '2' to run)")
    while decision != "1" or "2":
        if decision == "1":
            return combat_battle(character, foe)
        elif decision == "2":
            return cowardice_penalty(character)
        else:
            decision = input("There's no time for shenanigans! Enter '1' to fight or '2' to run!")


def foe_region_generator(character: dict) -> dict:
    """Extract a set of enemies from a list based on character location.

    :param character: a dictionary
    :precondition: character must be a dictionary that contains key-value pair 'location':string
    :postcondition: returns a random foe dictionary within a list in a list
    :return: a random dictionary that represents an enemy
    """
    if character['location'] == "Playground":
        return generate_foe()[0][random.randint(0, len(generate_foe()[0]) - 1)]
    elif character['location'] == "Cafeteria":
        return generate_foe()[1][random.randint(0, len(generate_foe()[1]) - 1)]
    elif character['location'] == "Teacher's Lounge":
        return generate_foe()[2][random.randint(0, len(generate_foe()[2]) - 1)]
    elif character['location'] == "Principal's Office":
        return generate_foe()[3][random.randint(0, len(generate_foe()[3]) - 1)]


def generate_foe() -> list:
    """Generate dictionaries based on unique enemies and store them in a list.

    :precondition: function must be called
    :postcondition: create several dictionaries and stores them in a list
    :return: a list called foe_list
    """
    lunch_lady = {'name': 'Lunch Lady', 'exp': int(LUNCH_LADY_MAX_HEALTH() * EXP_MULTIPLIER()),
                  'health': LUNCH_LADY_MAX_HEALTH(), 'MAX_DMG': LUNCH_LADY_MAX_DAMAGE(),
                  'attack': 'Twang! The Lunch Lady smacks you upside the head with a ladle!',
                  'death_message': 'The Lunch Lady retreats to the cafeteria!'}
    teacher = {'name': 'Teacher', 'exp': int(TEACHER_MAX_HEALTH() * EXP_MULTIPLIER()),
               'health': TEACHER_MAX_HEALTH(), 'MAX_DMG': TEACHER_MAX_DAMAGE(),
               'attack': 'Smack! The Teacher strikes you with a ruler!',
               'death_message': 'The Teacher retreats to the staff lounge!'}
    janitor = {'name': 'Janitor', 'exp': int(JANITOR_MAX_HEALTH() * EXP_MULTIPLIER()),
               'health': JANITOR_MAX_HEALTH(), 'MAX_DMG': JANITOR_MAX_DAMAGE(),
               'attack': 'Slop! The Janitor whips you with a dirty mop! Yuck!',
               'death_message': 'The Janitor retreats to the cleaning closet!'}
    class_clown = {'name': 'Class Clown', 'exp': int(CLASS_CLOWN_MAX_HEALTH() * EXP_MULTIPLIER()),
                   'health': CLASS_CLOWN_MAX_HEALTH(), 'MAX_DMG': CLASS_CLOWN_MAX_DAMAGE(),
                   'attack': 'Boom! The Class Clown hits you with some bad jokes!',
                   'death_message': 'The Class Clown has had his last laugh, he cowers in shame!'}
    bully = {'name': 'Bully', 'exp': int(BULLY_MAX_HEALTH() * EXP_MULTIPLIER()),
             'health': BULLY_MAX_HEALTH(), 'MAX_DMG': BULLY_MAX_DAMAGE(),
             'attack': 'Ouch! That Bully just made a "Yo Mama!" joke!',
             'death_message': 'The Bully runs away and cries for his Mommy!'}
    mean_girl = {'name': 'Mean Girl', 'exp': int(MEANGIRL_MAX_HEALTH() * EXP_MULTIPLIER()),
                 'health': MEANGIRL_MAX_HEALTH(), 'MAX_DMG': MEANGIRL_MAX_DAMAGE(),
                 'attack': 'Rude! The Mean Girl just made fun of your outfit!',
                 'death_message': 'The Mean Girl runs away to cry in the bathroom!'}
    teachers_pet = {'name': "Teacher's Pet", 'exp': int(TEACHERSPET_MAX_HEALTH() * EXP_MULTIPLIER()),
                    'health': TEACHERSPET_MAX_HEALTH(), 'MAX_DMG': TEACHERSPET_MAX_DAMAGE(),
                    'attack': "Thwap! The Teacher's Pet smacks you with a booklet full of optional "
                              "homework assignments!",
                    'death_message': "The Teacher's Pet runs to tell on you to the nearest Teacher!"}
    secretary = {'name': 'Secretary', 'exp': int(SECRETARY_MAX_HEALTH() * EXP_MULTIPLIER()),
                 'health': SECRETARY_MAX_HEALTH(), 'MAX_DMG': SECRETARY_MAX_DAMAGE(),
                 'attack': 'Clatter! The Secretary just hit you with their keyboard!',
                 'death_message': 'The Secretary runs to hide under their desk!'}
    playground_list = [class_clown, bully, mean_girl]
    cafeteria_list = [lunch_lady, janitor]
    teachers_lounge_list = [teacher, teachers_pet]
    principals_office_list = [teacher, secretary]
    return [playground_list, cafeteria_list, teachers_lounge_list, principals_office_list]


def cowardice_penalty(character: dict) -> dict:
    """Generate 20% chance for character to receive damage when they flee.

    :param character: a dictionary representing the user's character
    :precondition: character must be a dictionary with "health" key
    :precondition: "health" value must be an integer
    :postcondition: correctly modifies character's health value if necessary
    :return: character dictionary possibly with modified health value
    """
    initial_health = character['health']
    if random.randint(1, 100) <= 20:
        character["health"] -= random.randint(MIN_FLEE_DMG(), MAX_FLEE_DMG())
        print(f"\nDrats! You got hit in the back as you fled like a coward!"
              f" Your health has decreased from {initial_health} to {character['health']}.")
        time.sleep(2)
    else:
        print(f"\nYou have evaded the foes attempt to teach you a lesson! Good work!")
        time.sleep(2)
    return character


def combat_battle(character: dict, foe: dict) -> dict:
    """Begin combat battle between the player's character and foe.

    :param character: a dictionary representing the player's character
    :param foe: a dictionary representing the enemy
    :precondition: character and foe must be dictionaries
    :precondition: character must have key-value pairs: 'health':int, 'level':int, 'class':dict,
    'exp':int
    :precondition: 'class' dictionary must have key-value pairs: 'attack':string, 'MAX_DMG':tuple
    :precondition: foe must have key-value pairs: 'health':int, 'attack':string, 'MAX_DMG':int,
    'exp':int, 'death_message':string
    :precondition: elements in 'MAX_DMG' tuple must be integers
    :postcondition: correctly modifies character's health/exp/level values if necessary
    :return: character dictionary possibly with modified health/exp/level values
    """
    battle_ongoing = True
    while battle_ongoing:
        if keep_fighting():
            if foe_flee(foe):
                break
            combat_round(character, foe)
            if character["health"] <= 0 or foe["health"] <= 0:
                if foe["health"] <= 0:
                    print(f"\n{foe['death_message']}"), time.sleep(2)
                    gain_experience(character, foe)
                battle_ongoing = False
        else:
            cowardice_penalty(character)
            battle_ongoing = False
    return character


def keep_fighting() -> bool:
    """Ask user if they would like to fight or run.

    :return: a boolean
    """
    print("\nIt's your turn! Would you like to keep fighting or retreat?!")
    decision = input("Enter '1' to attack or '2' to flee!")
    while decision != "1" or "2":
        if decision == "1":
            return True
        elif decision == "2":
            return False
        else:
            decision = input("There's no time for shenanigans! Enter '1' to fight or '2' to run!")


def foe_flee(foe: dict) -> bool:
    """Generate 20% chance to determine if the foe will flee.

    :param foe: a dictionary representing the enemy
    :precondition: foe must have a key-value pair 'death_message':string
    :postcondition: returns True and prints flee statements if necessary
    :return: True or None
    """
    if random.randint(1, 100) <= 20:
        print(f"\nYour adversary has decided to flee!"), time.sleep(2)
        print(f"{foe['death_message']}")
        return True


def combat_round(character: dict, foe: dict):
    """Perform one round of combat.

    :param character: a dictionary representing the player's character
    :param foe: a dictionary representing the enemy
    :precondition: character and foe must be dictionaries
    :precondition: character must have key-value pairs: 'health':int, 'level':int, 'class':dict
    :precondition: 'class' dictionary must have key-value pairs: 'attack':string, 'MAX_DMG':tuple
    :precondition: foe must have key-value pairs: 'health':int, 'attack':string, 'MAX_DMG':int
    :precondition: elements in 'MAX_DMG' tuple must be integers
    :postcondition: correctly modifies character and foe ['health'] values if necessary
    :return: character and foe dictionaries possibly with modified health values
    """
    initiative = roll_initiative()
    player_first(character, foe) if initiative else enemy_first(character, foe)


def roll_initiative() -> bool:
    """Roll initiative for both combatants to determine first strike in combat round.

    :return: True or False or None
    """
    player_roll = random.randint(1, 100)
    enemy_roll = random.randint(1, 100)
    if player_roll > enemy_roll:
        return True
    elif enemy_roll > player_roll:
        return False
    else:
        print("You both parry each other's attack! No damage dealt!")


def player_first(character: dict, foe: dict):
    """Deal damage to enemy first in combat round.

    :param character: a dictionary representing the player's character
    :param foe: a dictionary representing the enemy
    :precondition: character and foe must be dictionaries
    :precondition: character must have key-value pairs: 'health':int, 'level':int, 'class':dict
    :precondition: 'class' dictionary must have key-value pairs: 'attack':string, 'MAX_DMG':tuple
    :precondition: foe must have key-value pairs: 'health':int, 'attack':string, 'MAX_DMG':int
    :precondition: elements in 'MAX_DMG' tuple must be integers
    :postcondition: correctly modifies character and foe ['health'] values if necessary
    :return: None
    """
    initial_player_health = character["health"]
    initial_enemy_health = foe["health"]
    foe["health"] -= random.randint(1, character['class']['MAX_DMG'][character['level'] - 1])
    print(f"\n{character['class']['attack']} {foe['name']}! Their health decreased from "
          f"{initial_enemy_health} to {foe['health']}."), time.sleep(2)
    if foe['health'] > 0:
        character["health"] -= random.randint(1, foe['MAX_DMG'])
        print(f"{foe['attack']} Your health decreased from "
              f"{initial_player_health} to {character['health']}."), time.sleep(2)


def enemy_first(character: dict, foe: dict):
    """Deal damage to player first in combat round.

    :param character: a dictionary representing the player's character
    :param foe: a dictionary representing the enemy
    :precondition: character and foe must be dictionaries
    :precondition: character must have key-value pairs: 'health':int, 'level':int, 'class':dict
    :precondition: 'class' dictionary must have key-value pairs: 'attack':string, 'MAX_DMG':tuple
    :precondition: foe must have key-value pairs: 'health':int, 'attack':string, 'MAX_DMG':int
    :precondition: elements in 'MAX_DMG' tuple must be integers
    :postcondition: correctly modifies character and foe ['health'] values if necessary
    :return: None
    """
    initial_player_health = character["health"]
    initial_enemy_health = foe["health"]
    character["health"] -= random.randint(1, foe['MAX_DMG'])
    print(f"\n{foe['attack']} Your health decreased from "
          f"{initial_player_health} to {character['health']}."), time.sleep(2)
    if character["health"] > 0:
        foe["health"] -= random.randint(1, character['class']['MAX_DMG'][character['level'] - 1])
        print(f"{character['class']['attack']} {foe['name']}! Their health decreased from "
              f"{initial_enemy_health} to {foe['health']}."), time.sleep(2)


def gain_experience(character: dict, foe: dict):
    """Add to character's 'exp' value.

    :param character: a dictionary representing the player's character
    :param foe: a dictionary representing an enemy
    :precondition: character and foe must be dictionaries
    :precondition: character and foe must have key-value pair: 'exp':int
    :return: None
    """
    character['exp'] += foe['exp']
    print(f"\nYou gained {foe['exp']} experience points for defeating that enemy!")
    time.sleep(2)
    check_level(character)


def check_level(character: dict):
    """Evaluate whether the player's character has levelled up.

    :param character: a dictionary representing the player's character
    :precondition: character must be a dictionary
    :precondition: character must have key-value pairs: 'name':string, 'level':int, 'exp':int, 'class':dict
    :precondition: 'class' dictionary must have key-value pairs: 'EXP_REQ':tuple of ints,
    'level_name':tuple of strings, 'MAX_HEALTH':tuple of ints, 'MAX_DMG':tuple of ints
    :postcondition: modifies the character's 'level' value and prints level up information if necessary
    :return: None
    """
    initial_level = character['level']
    if character['class']['EXP_REQ'][1] > character['exp'] >= character['class']['EXP_REQ'][0] \
            and character['level'] < 2:
        character['level'] = 2
    if character['exp'] >= character['class']['EXP_REQ'][1] and character['level'] < 3:
        character['level'] = 3
    if initial_level < character['level']:
        print(f"\nDing! Congratulations, {character['name']}! You have advanced to level {character['level']}!\n"
              f"You are now a {character['class']['level_name'][character['level'] - 1]}!\n"
              f"Your maximum health has increased to {character['class']['MAX_HEALTH'][character['level'] - 1]} "
              f"and maximum damage has increased to {character['class']['MAX_DMG'][character['level'] - 1]}.")
        time.sleep(5)


def heal_character(character: dict) -> dict:
    """Add to character's health value.

    :param character: a dictionary representing the player's character
    :precondition: character must be a dictionary
    :precondition: character must have key-value pairs: 'health': int, 'class':dict
    :precondition: 'class' dictionary must have key-value pairs: 'MAX_HEALTH':tuple of ints
    :postcondition: adds correct amount to character's 'health' value if necessary
    :return: character dictionary with possibly modified 'health' value

    >>> heal_character({"health": 10, "class": {"MAX_HEALTH": (20, 24, 28)}, "level": 1})
    <BLANKLINE>
    You rest in the hallway and regain your courage!
    Your health has increased from 10 to 14.
    {'health': 14, 'class': {'MAX_HEALTH': (20, 24, 28)}, 'level': 1}
    >>> heal_character({"health": 17, "class": {"MAX_HEALTH": (20, 24, 28)}, "level": 1})
    <BLANKLINE>
    You rest in the hallway and regain your courage!
    Your health has increased from 17 to 20.
    {'health': 20, 'class': {'MAX_HEALTH': (20, 24, 28)}, 'level': 1}
    >>> heal_character({"health": 20, "class": {"MAX_HEALTH": (20, 24, 28)}, "level": 1})
    {'health': 20, 'class': {'MAX_HEALTH': (20, 24, 28)}, 'level': 1}
    """
    initial_health = character["health"]
    if initial_health != character['class']['MAX_HEALTH'][character['level'] - 1]:
        character["health"] += 4
        if character["health"] > character['class']['MAX_HEALTH'][character['level'] - 1]:
            character["health"] = character['class']['MAX_HEALTH'][character['level'] - 1]
        print(f"\nYou rest in the hallway and regain your courage!\nYour health has "
              f"increased from {initial_health} to {character['health']}.")
        time.sleep(1.5)
    return character


def create_boss() -> dict:
    """Create dictionary to represent the game's boss.

    :return: a dictionary with key-value pairs: 'name':string, 'health':int, 'attack':string, 'MAX_DMG':int

    >>> create_boss()
    {'name': 'Principal', 'health': 50, 'attack': 'The Principal attacks you!', 'MAX_DMG': 15}
    """
    return {'name': 'Principal', 'health': BOSS_MAX_HEALTH(), 'attack': 'The Principal attacks you!',
            'MAX_DMG': BOSS_MAX_DAMAGE()}


def boss_battle(character: dict, boss: dict) -> dict:
    """Begin combat battle between the player's character and final boss.

    :param character: a dictionary representing the player's character
    :param boss: a dictionary representing the game's boss
    :precondition: character and boss must be dictionaries
    :precondition: character must have key-value pairs: 'health':int, 'level':int, 'class':dict
    :precondition: 'class' dictionary must have key-value pairs: 'attack':string, 'MAX_DMG':tuple
    :precondition: boss must have key-value pairs: 'health':int, 'attack':string, 'MAX_DMG':int
    :precondition: elements in 'MAX_DMG' tuple must be integers
    :postcondition: correctly modifies character and boss ['health'] values if necessary
    :return: the character dictionary possibly with modified 'health' value
    """
    boss_battle_ongoing = boss_level_check(character)
    riddle_asked = False
    while boss_battle_ongoing:
        while not riddle_asked:
            if riddle_question(character):
                boss['health'] = int(boss['health'] / 2)
                print("Principal Filbert: What?! How did you know that?! Barnacles! My health has been cut in half!")
            else:
                print("Principal Filbert: Muahaha! Perhaps if you studied more you would have known the answer!")
            riddle_asked = True
        combat_round(character, boss)
        time.sleep(2)
        if character['health'] <= 0 or boss['health'] <= 0:
            return character


def boss_level_check(character: dict) -> bool:
    """Check character's level to let the user decide to fight or flee.

    :param character: a dictionary
    :precondition: character must be a dictionary
    :precondition: character must have key-value pairs: 'level':int, 'current_coordinates':list of two ints
    :postcondition: asks user if they want to fight or flee
    :postcondition: returns True or False and edits character's current_coordinates if necessary
    :return: True or False
    """
    if character['level'] < 3:
        choice = input(f"The Principal is going to be a very tough opponent! \n Are you sure you are prepared? "
                       f"(Level 3 is recommended before beginning this fight! (Enter '1' to fight, '2' to run!)")
    else:
        choice = input("You've made it to the Principal's office! Are you prepared to face the Principal?"
                       " (Enter '1' to fight, '2' to run!)")
        time.sleep(2)
    while choice != "1" or "2":
        if choice == "1":
            return True
        elif choice == "2":
            character['current_coordinates'] = [BOSS_LOCATION()[0] - 1, BOSS_LOCATION()[1] - 1]
            return False
        else:
            choice = input("There's no time for shenanigans! Enter '1' to fight or '2' to run!")


def riddle_question(character: dict) -> bool:
    """Ask user to input answer for given riddle.

    :param character: a dictionary
    :precondition: character must be a dictionary
    :precondition: character must have key-value pairs: 'name':string, 'inventory':list
    :postcondition: determine if user's given input is correct answer
    :return: True or False
    """
    ascii_art.principal()
    time.sleep(2)
    print(f"Principal Filbert: Aha! I heard that you might be on your way here, {character['name']}.")
    time.sleep(2)
    print("Principal Filbert: I have a riddle for you... You are only allowed one guess before your detention begins."
          "\nYou will always find me in the past. I can be created in the present, but the future can never taint me. "
          "\nWhat am I?")
    time.sleep(2)
    if len(character['inventory']) > 0:
        print(f"The scraps of paper you picked up contain the letters: "
              f"{list(itertools.accumulate(character['inventory']))[-1]}... I wonder if they are clues?")
    answer = input(f"\n{character['name']}: ").lower()
    print(f"You got the letters: {set(filter(riddle_answer_letter_check, answer))} correct!")
    time.sleep(2)
    return True if answer == "history" else False


def riddle_answer_letter_check(guess: str) -> bool:
    """Check if string passed is in preset list of strings.

    :param guess: a string
    :precondition: guess must be a string
    :postcondition: checks if guess is in right_answer list
    :return: True or False

    >>> riddle_answer_letter_check('h')
    True
    >>> riddle_answer_letter_check('x')
    False
    """
    right_answer = ['h', 'i', 's', 't', 'o', 'r', 'y']
    return True if guess in right_answer else False


def game():
    """Start game."""
    character = make_character()
    board = make_board()
    boss = create_boss()
    notes = ['S', 'O', 'R', 'I', 'T', 'Y', 'H']
    while boss["health"] > 0 and character["health"] > 0:
        location(character, board, notes)
        direction = get_user_choice(character)
        valid_move = validate_move(character, direction)
        if valid_move:
            move_character(character, direction)
            if character['current_coordinates'] == list(BOSS_LOCATION()):
                boss_battle(character, boss)
            elif check_for_monsters():
                fight_or_flight(character)
            else:
                heal_character(character)
        else:
            print(f"Sorry, {character['name']}, that's not a valid option!"), time.sleep(1)
    if character["health"] <= 0:
        print("\nYour attempted coup against the administration has failed! "
              "You are going to be stuck in detention till the end of the school year! "
              "Better luck next time...")
    else:
        print(f"\nCongratulations, {character['name']}! The Principal has been defeated... "
              f"You have claimed the educational throne!")
    ascii_art.game_over_ascii()


def main():
    """Drives the program."""
    # doctest.testmod(verbose=True)
    game()


if __name__ == "__main__":
    main()
