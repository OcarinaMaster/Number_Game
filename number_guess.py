'''This is a number guessing game. 
I will write the psudo code before implementing the real code '''

import random

turn = 6
# Introduce yourself. Ask the player's name
print("Hi I am the number guessing robot.\n")
print("What is your name?")
# Let the player enter their name
pName = input()

# Ask the player it they want to play the game
print("Hi {}. It's very nice to meet you. Would you like to play a guessing game? Yes/No".format(pName))
pAnwer = input()
pAnwer = pAnwer.lower()
#if the player  Yes the start the game. If no then tell the user goodbye
if(pAnwer == "yes"):
    print("Ok {} lets play!!".format(pName) )
    print("Im gonna think of a number between 1 and 20")
else:
    print("Ok, bye {}...".format(pName))
    exit(0)


#Computer select a random number between 1 and 20.
ranint = random.randint(1,20)
print("{} Woopsee".format(ranint))
#The player has six truns.
#print("Make a guess of what I thought of")
#pGuess = input()


#For each turn Ask the user to guess the number

#If guess = number then tell the user they won.
#if (int(pGuess) == ranint):
    #print("Nice! Congratulations! You won!")
    
#else:
for i in range(0,turn):
    print("turn {}".format(i+1))
    pGuess = input()
    
            
    
        #I will loop here
    while (not pGuess.isnumeric()):
        print("Please type a number or you suck")
        pGuess = input()
    #else:
    if(int(pGuess) == ranint):
        print("Great Job!!!!!")
        break
    else:
        print("Ha sucka")
    if(i == turn - 1):
        print("well sorry sucka, you ran out of turns")
                    

    
#If guess <> number then tell the user too higher or too low and  to guess again

#If user runs out of guesses (After the 6th wrong guess)

#Tell the user the numer and to try again later.