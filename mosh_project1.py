"""Dice Rolling Exercise
Inout validation and corrective suggestions. Multiple random number generation"""
# Import packages
import random
# start the game
COUNTER = 0
while True:
    play = input('Are you ready to roll? Y or N: ').upper
    if play() == 'Y':
        COUNTER += 1
        die_1 = random.randint(1,6)
        die_2 = random.randint(1,6)
        print(f'The first die is {die_1}.')
        print(f'The second die is {die_2}.')
        print(f'The total of the two dice is {die_1 + die_2}.')
    elif play() == 'N':
        print('Thanks for playing!')
        break
    else:
        print('Invalid response. Please try again.')
print(f'You played {COUNTER} times.')
# End the game
#EOF
