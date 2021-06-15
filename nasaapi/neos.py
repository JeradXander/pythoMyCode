#!/usr/bin/python3
import requests



## Define NEOW 
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?start_date="
endofApi = "&api_key="
apilink = "&end_date="
finalapi = ""


def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/pythoMyCode/nasaapi/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = nasacreds.strip("\n")
    return nasacreds
# this is our main function
def main():

    key = returncreds()

    global  endofApi 
    
    endofApi = endofApi +  key
    ## build apikey
    global finalapi 


    date = input("please enter date in yyyy-mm-dd format\n")
    
    finalapi = NEOURL + date + apilink + date + endofApi
    


    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(finalapi)

    # strip off json attachment from our response
    neodata = neowrequest.json()
    
    numOfElements = neodata["element_count"]


    print(f"number of neos: {numOfElements}")
    
    neokeys = neodata["near_earth_objects"].keys()
    

    print(neokeys)

    
    ## display NASAs NEOW data
    #print(neodata)

if __name__ == "__main__":
    main()





