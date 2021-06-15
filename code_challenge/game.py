#!/usr/bin/python3
"""Jerad Alexander | This is my version of my game game is is a fork of Chads game """

#standard library

#3rd party libraries

from typing import Tuple
from Adventurer_file import Adventurer
from Monster_file import Monster
from rpsGame import game
# Replace RPG starter project with this code when new instructions are live

player1 = Adventurer("Mystery",100,"speed")
monster = Monster("Weird dragon",100,"strength")

def getadventur_stats(variable):
    """Method to get adv variables"""
    while True:
        userinput = ""
        if variable == "name":
            while userinput  == "":
                userinput = input("Greetings Adventurer!! What is your Name?\n>")

            return userinput
        elif variable == "ability":
            while userinput  == "" or userinput != "strength" and userinput != "intelligence":
                userinput = input("is your ability strength or Intelligence?!\n>")
                userinput = userinput.lower()
            return userinput

def intro():
    #print a main menu and the commands
    
    # get player info
    player1.name = getadventur_stats("name")
    player1.ability  = getadventur_stats("ability")
    
  
    #print out intro
    print(f'''\n\n
RPG Game
========
Player name:{player1.name} 
Player hp:{player1.HP} 
Player stats:{player1.ability} 
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            }
         }

#start the player in the Hall
currentRoom = 'Hall'

intro()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
      result_of_battle = game(player1,monster)
      
      if result_of_battle is True:
          print('You survived...now find a way out!')
          rooms[currentRoom]["item"] = "Dead " + monster.name
          
      elif result_of_battle is False:
          print('You DIED...GAME OVER!')
          break