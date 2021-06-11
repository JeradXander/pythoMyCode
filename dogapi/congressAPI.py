#!/usr/bin/env python3
"""Alta3 Research | Author: Jerad Alexander"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://holidayapi.com/v1/holidays?pretty&key=135fb821-56c7-41f8-aeca-27cdbe45047e&country=US&year=2020")

    print(r.json())

    # display the methods available to our new object
    print( dir(r) )
main()
