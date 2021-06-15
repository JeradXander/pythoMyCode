#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation


import requests


AOIF = "https://www.anapioficeandfire.com/api"

def main():
    gotresp = requests.get(AOIF)

    got_dj = gotresp.json()

    print(got_dj)


if __name__ == "__main__":

    main()
