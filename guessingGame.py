#usr/bin/python 
import math
import time
def playGame():
    print("I can guess the number you chosen in any range from 1 to whatever you want (; ")
    print("\n")
    r = int(raw_input("Enter the end of the range you choose from : "))
    print("\n")
    print("I can guess your number in at maximum "+ str(math.ceil(math.log(r,2)))+" attempts")
    print("\n")
    l = []
    for i in range(1,r+1):
        l.append(i)
    binarySearch(l)
def binarySearch(list):
    low = 0
    high = len(list)-1
    counter = 1
    while(low <= high):
        mid = ((low+high)/2)
        guess = str(raw_input("Is the number "+str(list[mid])+" [n/y]: "))
        if guess ==  "y" or guess == "Y":
            counter += 1
            print("Found your number in "+str(counter)+" guesses")
            break;
        elif guess == "n" or guess == "N":
            guess = str(raw_input("Is the number greater than "+str(list[mid])+"[n/y]"))
            if guess == "y" or guess == "Y":
                counter+=1
                low = mid+1
            elif guess == "n" or guess == "N":
                if list[mid] == 1:
                    print("Your selected number is not in range 1-"+str(r))
                    break;
                else:
                    counter +=1
                    high = mid -1
def MainMenu():
    print"""
    [1]Play the Game
    [2]Exit
    """
    choice = int(raw_input("Enter your choice: "))
    if choice == 1:
        playGame()
    elif choice == 2:
        print("So long!")
    else:
        print("Wrong choice please Enter a valid one!!")
        time.sleep(3)
        MainMenu()
MainMenu()
