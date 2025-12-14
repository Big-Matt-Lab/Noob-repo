"""Number Guessing Game
and coding example. Generating random numbers, comparative formulas
and directed suggestions"""

# Start the game
# Import package
import random

# Prompt user
AGAIN = True
print("Are you ready to play?")
print("Pick the high number.")
high_num = int(input())
# Generate random number
number = random.randint(1, high_num)
print(f"Guess a number between 1 and {high_num}:")
# Define boundaries
low_bound = 1
high_bound = high_num
# Start loop
while AGAIN:
    try:
        guess = int(input())
    except ValueError:
        print("Invalid Input. Please enter a number.")
        continue
    if guess < number:
        # Too low
        low_bound = max(low_bound, guess + 1)
        print("Too low. Try again.")
        print(f"Guess a number between {low_bound} and {high_bound}:")
    elif guess > number:
        # Too high
        high_bound = min(high_bound, guess - 1)
        print("Too high. Try again.")
        print(f"Guess a number between {low_bound} and {high_bound}:")
    else:
        # Success
        print(f"You got it! The number was {number}.")
        print("Would you like to play again? Y or N:")
        # Continue?
        play_again = input()
        if play_again.upper() == "Y":
            print("Pick the high number.")
            high_num = int(input())
            number = random.randint(1, high_num)
            low_bound = 1
            high_bound = high_num
            print(f"Guess a number between {low_bound} and {high_bound}:")
        else:
            # End the game
            AGAIN = False
# End of loop
print("Thanks for playing!")
# EOF
#
