""" An attempt to create a 'wordle' style game"""
import random

word_list = ['feel', 'dark', 'hear', 'cold', 'gone', 'list',
             'fine', 'cool', 'card', 'cute', 'life', 'hope', 'calm', 
             'away', 'say', 'hair', 'nine', 'exit', 'push', 'keep', 'fell', 
             'fact', 'city', 'sell', 'rice', 'four', 'game', 'busy', 'able', 
             'word', 'pull', 'back', 'five', 'baby', 'fair', 'base', 'hide', 'need', 'sale', 'chat']
word = random.choice(word_list)
print(word)
# guess = 'thin'
# if guess not in word_list:
 #   print("Not a word")
#else:
#    print("good word")

# TODO
# Use name - main
# Use functions
# Use proper
# Write intro and rules
# Use random.choice to choose a word
# Get user input
# Check against word list
# Check for character and positional matches
# Give feedback
# Loop input and checks
# Limit turns (loops)
# Value check - Try except for invalid characters - ValueError
# Incorporate an exit strategy during play
# Play again routine
# Expand word list
