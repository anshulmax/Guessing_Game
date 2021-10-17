# Anshul Anugu
# Purpose:Creating a number guessing game
# Instructions:
# Randomly choose a number between 1 and 100 (inclusive)
# Have the player enter a guess via input
# Tell the player the guess is high, low, or correct
# If high or low, allow the player to enter another guess
# Give the player an option to quit at any time
# Reward the player for a correct guess (ex., "Good job!")
# Tell the player how many guesses it took to guess correctly
from random import randint
# Create variables
random_number = randint(1, 100)
count_guess = 0
user_guess = ""
correct_guess = 0
# Print our instructions
print(f"Hello and Welcome to my Guessing Game! ")
print(f"Please enter a guess between 1 and 100. ")
print(f"I will tell you if your guess is too high or low to aid. ")
print(f"You can exit the game at any time by typing the letter 'q', but we hope this will not be the case! ")
print(f"Have fun and please share this with your friends! ")
print()
# Create a while loop with try statements inside
while correct_guess == 0:
    try:
        user_guess = input("What is your first guess? ")
        # Filter for just number values
        if str.isnumeric(user_guess):
            # Create a counter
            count_guess = count_guess + 1
            # Create number too low clause
            if int(user_guess) < random_number:
                print(f"{user_guess} is too low.  Guess again.")
            # Create number too high clause
            elif int(user_guess) > random_number:
                print(f"{user_guess} is too high.  Guess again.")
            # Create Number is spot on clause and show how many attempts
            else:
                print(f"{user_guess} IS CORRECT! CONGRATS! ")
                print(f"It took you {count_guess} guesses.")
                correct_guess = 1
        # Create q for quit option
        elif user_guess == "q":
            correct_guess = 1
        # Create clause in case they enter a non integer
        else:
            print(f"Please choose an integer between 1 and 100")
    except Exception as e:
        print(f"An error has occured. Please try again later.")
        correct_guess = 1
print(f"Game Over")