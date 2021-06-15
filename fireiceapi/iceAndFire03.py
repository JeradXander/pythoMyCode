#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        character = gotresp.json()

        numberofseasons = len(character["tvSeries"])


        if character["name"] ==  "":

            print(f"""{character["aliases"][0]} is in {numberofseasons} seasons!""")
        else:
            print(f"""{character["name"]} is in {numberofseasons} seasons!""")

        

if __name__ == "__main__":
        main()

