import char

# Central File that holds the central game logic
game_running = False

def new_game():
    pass

def load_game():
    pass

def save_game():
    pass

def delete_save():
    pass

def game_loop():
    game_running = True
    while game_running:
        print("Theta Character Test (ALPHA V0.01)")
        print("1. New Character")
        print("2. Exit")
        test = input("What would you like to do?")
        if test == "1":
            print("What stats would you like?")
            print("Stats are: Health, Physical, Special, Wit, and Speed")
            print("Stats have to add up to 50")
            test2 = input("What would you like your stats to be?")
            test22 = test2.split()
            if len(test22) == 5:
                print("Character made.")
                myChar = char.Player("TEST", 1, char.CharStats(test22[0], test22[1], test22[2], test22[3], test22[4]))
                print("Your Stats", myChar.my_CharStats.getStatLine())
                game_running = False
        elif test == "2":
            game_running = False
        else:
            print("Unrecognized input")

game_loop()

