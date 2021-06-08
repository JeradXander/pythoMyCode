#!/usr/bin/env python3

import winningLogic
import random

#list of possible moves that user can select
moves = ["rock","paper", "scissors","lizard", "spock"]

userScore = 0
comScore = 0
valid = False


while not valid:
    x=1
    
    print("\nRock, Paper, Scissors, Lizard, Spock")
    print("---------------------------------------------------------------------")

    while x < len(moves) +1:
        print(f"{x}. {moves[x-1]}")
        x+=1
    moveSelected = input("\nPlease select a move from the list above\n(type the number associated with the move i.e 1 for rock)\n")
    
    try: 
        val = int(moveSelected) - 1
        if val < len(moves)  and val > -1:
            print(f"\nYou selected {moves[val].capitalize()}")

            compMove = random.randint(0, len(moves)-1)
            print(f"The computer selected {moves[compMove].capitalize()}\n")


            result = winningLogic.result(val,compMove)
            print(f"The result was a {result}!!")

            if result == "win":
                userScore += 1
            elif result == "loss":
                comScore += 1

            
            print(f"The score is:\nYour Score - {userScore}\nComputer Score - {comScore}\n\n")
            
            exit = input("hit x then Enter to finish game or anything else and enter to continue")

            if exit == "x":
                valid = True
            else:
                continue  
            
        else:
             print("You need to select a move from the list above\n(type the number associated with the move i.e 1 for rock): TRY AGAIN\n\n")
             continue
    
    except ValueError:
            print("You need to select a move from the list above\n(type the number associated with the move i.e 1 for rock): TRY AGAIN\n\n")
            continue
