# File that will hold tables of info based on location to allow for certain events to occur in certain places
# Will affect Characters (Player and maybe more)
import char as Char

# List of Events for each location

class Event:
    def __init__(self, name):
        self.name = name
        # Event Type - What the event does (i might make this an int)
        # One for moving locations, two stats stuff, three
        # Array of stats effected


'''
def game_init(passed_char):
    pass

def game_loop_func():
    game_layer = 0
    print("")

'''