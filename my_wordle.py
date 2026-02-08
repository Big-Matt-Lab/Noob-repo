""" An attempt to create a 'wordle' style game"""
import random
import sys

WORD_LIST = [
  'feel', 'dark', 'hear', 'cold', 'gone', 'list',
  'fine', 'cool', 'card', 'cute', 'life', 'hope', 'calm', 
  'away', 'say', 'hair', 'nine', 'exit', 'push', 'keep', 'fell', 
  'fact', 'city', 'sell', 'rice', 'four', 'game', 'busy', 'able', 
  'word', 'pull', 'back', 'five', 'baby', 'fair', 'base',
  'hide', 'need', 'sale', 'chat'
]

MAX_GUESSES = 5 # Change Max guesses to whatever practical number you need

def get_secret_word() -> str:
    """ Selects the secret word from a list
    no params
    returns: chosen word"""

    word = random.choice(WORD_LIST)
    return word

def intro():
    """ Opening greeting and explanation """


def get_users_word() -> str:
    """ Input routine 
    called by loop.
    no params
    # guess = 'thin'
    # if guess not in word_list:
    #   print("Not a word!")
    returns word (str)"""

    num_guesses = 0
    while num_guesses <= MAX_GUESSES:
        guess = ''
        # keep looping until valid guess
        while len(guess) != 4 or not guess.isalpha():
            print('Guess #{}: '.format(num_guesses))
            guess = input('> ')
            if guess == 'q':
                print("Thanks for playing!")
                sys.exit()
            return guess

def get_clues(guess: str, secret_word: str) -> str:
    """ Check routine
    checks character by character for match and 
    provides feedback to user.
    param: guess: users input (str)
    param: secret_word: randomly selected secret word. 
    returns: feedback"""

    if guess == secret_word:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            # A correct letter is in the correct place
            clues.append('Fermi')
        elif guess[i] in secret_word[i]:
            # A correct letter is in the incorrect place
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # There are no correct digits at all
    else:
        # Sort the clues into alphabetical order so their order
        # doesn't give anything away
        clues.sort()
        # Make a single string from the list of clues
        return ' '.join(clues)


def main():
    """ Main program """
    intro()

    secret_word = get_secret_word()

    while True:
        print("The word has been chosen. Begin.")

        guess = get_users_word()
        get_clues(guess, secret_word)


# TODO

# write intro and rules
# Get user input
# Check for character and positional matches
# Give feedback
# Loop input and checks
# Limit turns (loops)
# Value check - Try except for invalid characters - ValueError
# Incorporate an exit strategy during play
# Play again routine
# Expand word list
if __name__ == "__main__":
    main()

# EOF
