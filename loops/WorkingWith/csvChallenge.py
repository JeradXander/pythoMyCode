#!/usr/bin/env python3
"""CSV Challenge reading and writing food data"""

# standard library import
import csv

#lists to add data too
boysList = []
girlsList = []


with open("babyName.csv","r") as names:

    #variables 
    ind = 0
    year = 2000 
    haveGirl = False
    rowNumber = 0
    #for loop to loop through names
    for row in csv.reader(names):
        
        rowNumber += 1
        #skipping first legend row
        if ind ==0:
            ind += 1
            continue
        
        else:
        
            #skipping first row which is the legend
            if len(row) != 0:

                #if current row is eqauls to year wanted
                if int(row[0]) == year:

                    if row[2] == "F" and haveGirl is False:
                        #adding girl to List
                        girlsList.append(f"{row[1]} was the most popular girls name in the year {row[0]} with {row[3]} girls being named that!!\n")
                        ind += 1
                        haveGirl = True
                        
                    elif row[2] == "M":
                        #increasing variables
                        year +=1
                        ind +=1
                        #adding boys to list
                        boysList.append(f"{row[1]} was the most popular boys name in the year {row[0]} with {row[3]} girls being named that!!\n")
                        haveGirl = False


#writing most popular names 
with open ("mostPopularNames", "w") as popFile:
    
    #writing girls names
    print("Girls Name",file=popFile)
    print("-"* 30,file=popFile )
    for girls in girlsList:
        print(girls,file=popFile)

    #writing boys names 
    print("\n\nBoys List", file=popFile)    
    print("-"* 30,file=popFile )
    for boys in boysList:
        print(boys,file=popFile)


#output to let user know file was saved
print(f"mostPopularNames file created from {rowNumber} names")


