#!/usr/bin/env python3


farms = [{"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "E Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]}]


def loopthroughNE():
    for x in farms:
        if x["name"] == "NE Farm":

            farmName = x["name"]
            for anim in x["agriculture"]:
                print(f"animal/crops in {farmName} is {anim}")




def chooseFarm():

    valid = False

    while not valid:
        
        uInput = input("\nPlease Type in (NE Farm / W Farm / E Farm / SE Farm) to visit to see the agriculture\n")






        if uInput == "E Farm" or uInput == "NE Farm" or uInput == "W Farm" or uInput == "SE Farm" :
            
            for x in farms:
                
                if x["name"] == uInput:
                    
                    farmName = x["name"]
                    
                    for anim in x["agriculture"]:
                        
                        print(f"animal/crop in {farmName} is {anim}")
                        valid = True
                    
        else:
            print("Not a valid selection please Type exactly how they are spelled inclding capital")
            continue


def chooseFarmAnim():

    valid = False

    while not valid:

        uInput = input("\nPlease Type in (NE Farm / W Farm /E Farm / SE Farm) to visit to see just the animals\n")

        if uInput == "E Farm" or uInput == "NE Farm" or uInput == "W Farm" or uInput == "SE Farm":

            for x in farms:

                if x["name"] == uInput:

                    farmName = x["name"]

                    for anim in x["agriculture"]:
                        
                        if anim != "carrots" and anim != "bananas" and anim != "apples" and anim != "oranges" and anim != "celery":
                            
                            print(f"animal in {farmName} is {anim}")
                            valid = True
                        else:
                            print("There are no animals just produce")
                            valid = True
        else:
            print("Not a valid selection please Type exactly how they are spelled inclding capital")
            continue


loopthroughNE()

chooseFarm()

chooseFarmAnim()
