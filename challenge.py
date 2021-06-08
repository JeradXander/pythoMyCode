#!/usr/bin/env python3

import random

icecream= ["flavors", "salty"] 
tlgclass= ["Brian","Clint","Damian","Dan","David","Jelani","Jerad","Jon","Jun","Mark","Max"]

icecream.append(99)

while True:
    userSelection =  input("Please type a number in the range of 0-10 ")
    userInt = int(userSelection)
    if userInt  < 11 and userInt > -1:
         print(f"{icecream[-1]} {icecream[0]} and {tlgclass[userInt]} chooses to be salty!!")
         break
    else:
        print("Please enter a number between in the range of 0-10")

print(f"{icecream[-1]} {icecream[0]} and {tlgclass[random.randint(0,9)]} chooses to be salty")


