#!/usr/bin/env python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""
import requests

APIURI = "http://api.open-notify.org/astros.json"
astroList = [];

def main():
    
    apirequest = requests.get(APIURI)
    reqToJSON = apirequest.json()
    numberOfAstros = reqToJSON["number"]
    print(f"There are {numberOfAstros} in space currently")
    
    for astros in reqToJSON["people"]:
        
        name = astros["name"] 
        craft = astros["craft"]
        astroList.append({"namekey": name, "craftkey": craft})
        
        print(f"{name} is currently in space on the {craft}")
        
if __name__ == "__main__":
    main()
    print(astroList)
        