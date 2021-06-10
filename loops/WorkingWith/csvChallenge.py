#!/usr/bin/env python3
"""CSV Challenge reading and writing food data"""

# standard library import
import csv


boysList = []
girlsList = []


with open("babyName.csv","r") as names:

    ind = 0
    year = 2000 
    haveGirl = False
    for row in csv.reader(names):
        
        
        if ind ==0:
            ind += 1
            continue
        
        else:
        

            if len(row) != 0:
                if int(row[0]) == year:

                    if row[2] == "F" and haveGirl is False:
                        
                        girlsList.append(f"{row[1]} was the most popular girls name in the year {row[0]} with {row[3]} girls being named that!!\n")
                        ind += 1
                        haveGirl = True
                        
                    elif row[2] == "M":
                        year +=1
                        ind +=1
                        boysList.append(f"{row[1]} was the most popular boys name in the year {row[0]} with {row[3]} girls being named that!!\n")
                        haveGirl = False

with open ("mostPopularNames", "w") as popFile:

    print("Girls Name",file=popFile)
    print("-"* 30,file=popFile )
    for girls in girlsList:
        print(girls,file=popFile)

    
    print("\n\nBoys List", file=popFile)    
    print("-"* 30,file=popFile )
    for boys in boysList:
        print(boys,file=popFile)



print("mostPopularNames file creates")


