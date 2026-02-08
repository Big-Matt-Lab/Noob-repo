"""Bageels, by Al Sweigart
A deductive logic game where you must guess a number based on clues.
"""

import random
import sys
NUM_DIGITS = 2
MAX_GUESSES = 10

def main():
    print(f'''Bageels, a deductive logic game.
By Al Sweigart


I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.end
Try to guess what it is. Here are some clues:
When I say:      That means:
  Pico      One digit is correct but in the wrong position.
  Fermi     One digit is correct and in the right position.
  Bagels    No digit is correct.  

  For example, if the secret number was 248 and your guess was 843, the
  clues woud be Fermi, Pico.''')
    while True: # Main game loop
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(f'You have {MAX_GUESSES} guesses to get it.')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until a falid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
                if guess == 'q':
                    sys.exit()

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # Correct, break out of this loop
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses")
                print('The answer was {}.'.format(secretNum))

        # Ask if player wnats to play again
        print("Do you want to play again? (yes or no)")
        if not input('> ').lower().startswith('y'):
            break
    print("Thanks for playing!")

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique, random digits."""
    numbers = list('0123456789') # Create list of digits
    random.shuffle(numbers) # SHuffle into random order

    # Get the first digits
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the 'pico', 'fermi', and 'bagel' clues for a
    guess and secret number pair"""
    if guess == secretNum:
        return "You got it!"
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect lpace
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # There are no correct digits at all
    else:
        # Sort the clues into alphabetical order so their order 
        # doesn't give anything away
        clues.sort()
        # Make a single string from the list of clues
        return ' '.join(clues)
    
# If the program is run (instead of imported), run the game
if __name__ == '__main__':
    main()

    # EOF
