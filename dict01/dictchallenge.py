#!/usr/bin/env python3

heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "magic",
    "archenemy": "Voldemort",},
"captain america":
    {"real name": "Steve Rogers",
    "powers": "frisbee shield",
    "archenemy": "Hydra",}
        }




char_name = input("Which character do you want to know about? (Wolverine, Harry Potter, Captain America)")

char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")

while char_name not in heroes.keys():
            print("Please enter a valid hero name:")
            char_name = input("hero name: ")
            char_name = char_name.lower()
                     


while char_stat not in heroes[char_name].keys():
            print("Please enter a valid hero stat:")
            char_stat = input("hero stat: ")
            char_stat = char_stat.lower()

print(f"{char_name.capitalize()}'s {char_stat} is: {heroes[char_name][char_stat]}")

hero={'name':{'alias':'Batman','real name':'Bruce Wayne'},'background':{'origin':'Parents got murdered, got angry. Is super rich.','family':{'parents':'dead','siblings':None},'age':32,'number of deaths':19},'powers':['ninja training','money','batsuit'],'enemies':['joker','two face','scarecrow','poison ivy'],'allies':['cat woman','red robin','nightwing'],'rivals':['joker'],'weaknesses':['poverty','strict moral code']}


userinput = input("What would you like to see of batman (enemies, allies, rivals, powers, or weaknesses)")

batmanList = hero[userinput]

for x in batmanList:
  print(f"Batman's {userinput}: {x}")



