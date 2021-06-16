#!/usr/bin/env python3 

def main():

    ind = 1 

    oddNumber = 7
    
    starNumber = 1
    
    if oddNumber % 2 != 0:
        
        for i in range(oddNumber):
    
            if i != oddNumber / 2 + .5 and i < oddNumber / 2 + .5 -1 :
                
                print("*"* starNumber)
                starNumber+=1
            elif i != oddNumber / 2 + .5 and i > oddNumber / 2 + .5 -1:
                print("*"* starNumber)
                starNumber-=1
            else:
                print("*"* starNumber)
                starNumber-=1
    else:
        print("oddnumber needs to be odd")


if __name__ == "__main__":
    main()
