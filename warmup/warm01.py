#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.

def add(calc1,calc2):
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))


def sub(calc1,calc2):
        print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))


def main():
    while True:

        print("\nWhat is the first operator? Or, enter q to quit: ")
        calc1 = input(),lower()
        if calc1 == "q":
            break
        calc1 = float(calc1)
        print("\nWhat is the second operator? Or, enter q to quit: ")
        calc2 = input().lower()
        if calc2 == "q":
            break
        calc2 = float(calc2)
        print("Enter an operation to perform on the two operators (+ or -): ")
        operation = input()
        if operation == "+":
            add(calc1,calc2)
        elif  operation == '-':
            sub(calc1,calc2)
        else:
            print("\n Not a valid entry. Restarting...")

if __name__ == "__main__"

main()
