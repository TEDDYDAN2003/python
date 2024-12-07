import random
import time
from os import system

MAX_ATTEMPT= 10
MIN_NUMBER= 1
MAX_NUMBER= 50

def introduction():
    '''this is the introduction function for our program !'''
    print("YOU WILL GET 10 ATTEMPTS IN THIS GAME !")
    print("\n IN 10 ATTEMPTS YOU ARE REQUIRED TO COME UP WITH THE RANDOM NUMBER THAT AI GENERETED !")
    for count in range(1,4): 

        print(count)
        time.sleep(1)
    print("READY OR NOT HERE WE GO ! ")        
    time.sleep(2)
    system("cls")
def play_number_guesssing_game():
    num=random.randint(MIN_NUMBER,MAX_NUMBER)
    guess_list=[]

    attempt=1
    while attempt != (MAX_ATTEMPT +1):
        try:
            guess=int(input("GUESS A NO. :"))
        except ValueError:
            print("ENTER A VALID NUMBER!")    
            continue
        if guess==num:
            print(f"\n YOU GOT IT RIGHT IN {attempt}.\n the no. is {num} ")
            return
        elif guess> num:
            print(f"the number is less than {guess}")
            attempt +=1
            print(11-attempt , "attempts left")
        elif guess< num:
            print(f"the number is greater  than {guess}")
            attempt +=1
            print(11-attempt , "attempts left")
        elif guess in guess_list:
            print("you already guessed this number before: ")
        guess_list.append(guess)

    if attempt>=10:
        system("cls")
        print("YOU ARE A FAILURE! ")
        print("GAME IS OVER !")
        print(f"The correct number is {num}")
introduction()
play_number_guesssing_game()


