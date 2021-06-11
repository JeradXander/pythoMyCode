#!/usr/bin/env python3 





def main():

    ind = 1 

    while ind < 101:
        
        if ind %3 ==0 and ind %5==0:
            print("FizzBuzz")
            ind += 1

        elif ind % 3==0:
            print("Fizz")
            ind += 1 
        elif ind % 5==0:
            print("Buzz")
            ind += 1
        else:
            print(ind)
            ind += 1

main()
