#!/usr/bin/env python3

import winningLogic
import random

#list of possible moves that user can select
moves = ["rock","paper", "scissors","lizard", "spock"]

#variables
userScore = 0
comScore = 0
valid = False

#while loop for the game and valid inputs
while not valid:
    x=1
    
    #outputs
    print("\nRock, Paper, Scissors, Lizard, Spock")
    print("---------------------------------------------------------------------")

    #loop to show moves
    while x < len(moves) +1:
        print(f"{x}. {moves[x-1]}")
        x+=1

    #getting user input    
    moveSelected = input("\nPlease select a move from the list above\n(type the number associated with the move i.e 1 for rock)\n")
    
    #try to convert string to int
    try: 

        #setting input to int
        val = int(moveSelected) - 1

        #condiotional if int is a valid move
        if val < len(moves)  and val > -1:

            print(f"\nYou selected {moves[val].capitalize()}")

            #getting random computer move
            compMove = random.randint(0, len(moves)-1)

            #output to user
            print(f"The computer selected {moves[compMove].capitalize()}\n")

            #using imported function to get result sending user move and computer moves
            result = winningLogic.result(val,compMove)
            print(f"The result was a {result}!!")

            #conditional for score
            if result == "win":
                userScore += 1
            elif result == "loss":
                comScore += 1

            #score output
            print(f"The score is:\nYour Score - {userScore}\nComputer Score - {comScore}\n\n")
            
            #exit input
            exit = input("hit x then Enter to finish game or anything else and enter to continue")
           
           #exit conditional
            if exit == "x":
                valid = True
            else:
                continue  

        #if inouts are invalid 
        else:
             print("You need to select a move from the list above\n(type the number associated with the move i.e 1 for rock): TRY AGAIN\n\n")
             continue
    
    except ValueError:
            print("You need to select a move from the list above\n(type the number associated with the move i.e 1 for rock): TRY AGAIN\n\n")
            continue
