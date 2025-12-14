""" Number Guessing Game
and coding example. Generating random numbers, comparative formulas
and directed suggestions"""
# Start the game
# Import package
import random
# Prompt user
AGAIN = True
print('Are you ready to play?')
print('Pick the high number.')
high_num = int(input())
print('Guess a number between 1 and 50:')
# Start loop
while AGAIN:
    guess = int(input())
    if guess < number:
        # Too low
        print('Too low. Try again.')
        print(f'Guess a number between {guess + 1} and 50:')
    elif guess > number:
        # Too high
        print('Too high. Try again.')
        print(f'Guess a number between 1 and {guess - 1}:')
    else:
        # Success
        print('You got it!')
        print('Would you like to play again? Y or N:')
        # Continue?
        play_again = input()
        if play_again == 'Y':
            AGAIN = True
        else:
            # End the game
            AGAIN = False
# End of loop
print('Thanks for playing!')
# EOF
#

