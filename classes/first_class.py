#!/usr/bin/env python3 
"""Jerad Alexander | First class"""

#standard imports
from random import randint
#thrid party imports

class Player:
    def __init__(self):
        self.dice = []


    def roll(self):
        self.dice = [] #clear current dice

        for i in range(3):
            self.dice.append(randint(1,6))  #1 to6 dice


    def get_dice(self): #return the dice rolls
        return self.dice


def main():
    """called at runtime"""

    ##create our players

    player1 = Player()
    player2 = Player()

    player1.roll()
    player2.roll()

    print(f"Plpayer 1 rolled {player1.get_dice()}")
    print(f"Player 2 rolled {player2.get_dice()}")

    if sum(player1.get_dice()) == sum(player2.get_dice()):
        print("Draw!!")

    elif sum(player1.get_dice()) > sum(player2.get_dice()):
        print("Player 1 wins")

    elif sum(player1.get_dice()) < sum(player2.get_dice()):
        print("Player 2  wins")
            

if __name__  == "__main__":
    main()
