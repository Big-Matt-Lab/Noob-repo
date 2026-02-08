""" An attempt to create a 'wordle' style game"""
import random
import sys

WORD_LIST = [
  'feel', 'dark', 'hear', 'cold', 'gone', 'list',
  'fine', 'cool', 'card', 'cute', 'life', 'hope', 'calm', 
  'away', 'hair', 'nine', 'exit', 'push', 'keep', 'fell', 
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


def get_users_word():
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
            print(f'Guess #{num_guesses}: ')
            guess = input('> ')
            guess = guess.lower()
            if guess == 'q':
                print("Thanks for playing!")
                sys.exit()
            return guess

def get_clues(guess, secret_word):
    """ Check routine
    checks character by character for match and 
    provides feedback to user.
    param: guess: users input (str)
    param: secret_word: randomly selected secret word. 
    returns: feedback"""

    if guess == secret_word:
        return "You got it!"

    clues = []

    for i, char in enumerate(guess):
        if char == secret_word[i]:
            # A correct letter is in the correct place
            clues.append('Correct ')
        elif char in secret_word:
            # A correct letter is in the incorrect place
            clues.append('Close ')
        else:
            clues.append('No ')

    return clues


def main():
    """ Main program """
    intro()

    secret_word = get_secret_word()
    print("The word has been chosen. Begin.")
    print(secret_word) # REMOVE THIS BEFORE FINAL
    guesses = 1

    while guesses <= MAX_GUESSES:
        guess = get_users_word()
        feedback = get_clues(guess, secret_word)
        print(feedback)
        if guess == secret_word:
            break
        guesses += 1


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
