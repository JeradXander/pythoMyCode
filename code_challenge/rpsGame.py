#!/usr/bin/env python3

import winningLogic
import random

from Adventurer_file import Adventurer


def game (adventurer, monster):
    
    player = adventurer
    current_monster = monster
    #list of possible moves that user can select
    moves = ["rock","paper", "scissors"]

    #variables
    userScore = 0
    comScore = 0
    valid = False

    print(f"""\nOh no!! A {current_monster.name} appeared\nand challenged you to a game of\n""")

    #while loop for the game and valid inputs
    while not valid:
        x=1
        
        #outputs
        print(f"""\nRock, Paper, Scissors to the DEATH!!!!!!!!!""")
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
                print(f"The {current_monster.name} selected {moves[compMove].capitalize()}\n")

                #using imported function to get result sending user move and computer moves
                result = winningLogic.result(val,compMove)
                print(f"The result was a {result}!!")

                #conditional for score
                if result == "win":
                    
                    if player.ability == "strength" and monster.weakness == "strength":
                        
                        userScore += 1
                        print(f"{player.name}'s strength is {monster.name}'s weakness and did 10 more damage because of pure aggression")
                        monster.HP -= 30
                        
                        if monster.HP < 1:
                            print(f"You defeated the {monster.name}")
                            return True

                    elif player.ability == "intelligence" and monster.weakness == "intelligence":
                        userScore += 1
                        print(f"{player.name}'s strength is {monster.name}'s weakness and outsmarted it for 5 more damage and grabbed a scale to add 5hp of armor")
                        monster.HP -= 25
                        player.HP += 5
                        if monster.HP < 1:
                            print(f"You defeated the {monster.name}")
                            return True
                        
                    
                elif result == "loss":
                    comScore += 1
                    print(f"The {monster.name}'s breath fire on you and did 20 damage to you ")
                    player.HP -= 20
                    
                    if player.HP < 1:
                            print(f"You were defeated by the {monster.name}")
                            return False
                    

                #score output
   #             print(f"The score is:\nYour Score - {userScore}\nComputer Score - {comScore}\n\n")
                
                #exit input
   #             exit = input("hit x then Enter to finish game or anything else and enter to continue")
            
            #exit conditional
                # if exit == "x":
                #     valid = True
                # else:
                #     continue  
            
            #if inouts are invalid 
            else:
                print("You need to select a move from the list above\n(type the number associated with the move i.e 1 for rock): TRY AGAIN\n\n")
                continue
        
        except ValueError:
                print("You need to select a move from the list above\n(type the number associated with the move i.e 1 for rock): TRY AGAIN\n\n")
                continue
