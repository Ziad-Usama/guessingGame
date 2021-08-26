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
    low =0
    high = len(list)-1
    counter = 0
    while(low <=high):
        mid = ((low+high)/2)
        guess = str(raw_input("Is the number ([G]reater/ [S]maller/ [E]qual) to "+str(list[mid])+": "))
        if guess == "G" or guess == "g":
            if(list[mid] == r):
                print("Your number isn't in range")
            else:
                counter +=1
                low = mid + 1
        elif guess == "S" or guess == "s":
            if list[mid] == 1:
                print("Your selected number is not in range ")
                break;
            else:
                counter += 1
                high = mid - 1
        elif guess == "E" or guess == "e":
            counter += 1
            print("Found your number in "+str(counter)+" attempts")
            break;
        else:
            print("please enter a valid choice!!!")
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
