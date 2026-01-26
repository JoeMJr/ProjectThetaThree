# Going to use dictonaries to quickly go between menus instead of if statements
import char

menu_code = 0
menu_dict = {0 : dev_menu,
             1 : start_menu}

def game_menus():
    pass

def dev_menu():
    print("THIS IS DEV MENU SOMETHING WENT WRONG")
    return 0

def start_menu():
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
        return False
    else:
        print("Unrecognized input")