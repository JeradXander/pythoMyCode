#!usr/bin/env python3

#winningLogic 
def result(user,comp):

    #conditional for user move
    #rock
    if user == 0:
        #condiotional for comp moves
        if comp == 0:
            return "draw"

        elif comp == 1:
            print("Paper covers Rock")
            return "loss"
       
        elif comp == 2:
            print("Rock crushes Scissors")
            return "win"
    #paper
    elif user == 1:
        
        if comp == 1:
            return "draw"

        elif comp == 0:
            print("Paper covers Rock")
            return "win"
        elif comp == 2:
            print("Scissors cuts Paper")
            return "loss"
      
    #scissors
    elif user == 2:

        if comp == 2:
            return "draw"
        elif comp == 0:
            print("Rock crushes Scissors")
            return "loss"
        elif comp == 1:
            print("Scissors cuts Paper")
            return "win"
       

    
