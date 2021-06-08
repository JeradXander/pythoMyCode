#!usr/bin/env python3

#winningLogic 
def result(user,comp):
    if user == 0:

        if comp == 0:
            return "draw"

        elif comp == 1:
            print("Paper covers Rock")
            return "loss"
        elif comp == 4:
            print("Spock vaporizes Rock")
            return "loss"
        elif comp == 3:
            print("Rock crushes Lizard")
            return "win"
        elif comp == 2:
            print("Rock crushes Scissors")
            return "win"

    elif user == 1:
        
        if comp == 1:
            return "draw"

        elif comp == 0:
            print("Paper covers Rock")
            return "win"
        elif comp == 2:
            print("Scissors cuts Paper")
            return "loss"
        elif comp == 3:
            print("Lizard eats Paper")
            return "loss"
        elif comp == 4:
            print("Paper disproves Spock")
            return "win"

    elif user == 2:

        if comp == 2:
            return "draw"
        elif comp == 0:
            print("Rock crushes Scissors")
            return "loss"
        elif comp == 1:
            print("Scissors cuts Paper")
            return "win"
        elif comp == 4:
            print("Spock smashes Scissors")
            return "loss"
        elif comp == 3:
            print("Scissors decapitates Lizard")
            return "win"
    elif user == 3:

        if comp == 0:
            print("Rock crushes Lizard")
            return "loss"
        elif comp == 1:
            print("Lizard eats Paper")
            return "win"
        elif comp == 2:
            print("Scissors decapitates Lizard")
            return "loss"
        elif comp == 3:
            return "draw"
        elif comp == 4:
            print("Lizard poisons Spock")
            return "win"
    elif user == 4:
        if comp == 0:
            print("Spock vaporizes Rock")
            return "win"
        elif comp == 1:
            print("Paper disproves Spock")
            return "loss"
        elif comp == 2:
            print("Spock smashes Scissors")
            return "win"
        elif comp == 3:
            print("Lizard poisons Spock")
            return "loss"
        elif comp == 4:
            return "draw"

