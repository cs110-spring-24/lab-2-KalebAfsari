import random

user = 0
play = "yes"

while play == "yes":   
    guess = 0
    min = 1
    max = 100
    cpu = random.randint(1, 100)
    while user != cpu:
        guess = guess + 1
        strmin = str(min)
        strmax = str(max)
        user = input("Guess a number between " + strmin + " and " + strmax +":")
        user = int(user)

        if user > cpu:
            max = user
            print("Too high!")
        elif user < cpu:
            min = user
            print("Too low!")
        else:
            print("You got it in" , guess, "guesses!")
    
    play = input("Would you like to play again?")
print("Goodbye!")
    



    


