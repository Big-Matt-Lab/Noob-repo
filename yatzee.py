

import random


def roll_dice(num_dice):
    """Rolls a specified number of dice and returns a list of results."""
    return [random.randint(1, 6) for _ in range(num_dice)]

def reroll_selected(my_dice, indices_to_reroll):
    """Rerolls dice at specific indices in a list and updates the list."""
    dice_list = my_dice
    for index in indices_to_reroll:
        if 0 <= index < len(dice_list):
            # Roll a new die and update the list at that specific index
            dice_list[index] = random.randint(1, 6)
        else:
            print(f"Warning: Index {index} is out of bounds and was ignored.")
    return dice_list


my_dice = roll_dice(5)
	
print(my_dice)

dice_to_reroll = input('dice to reroll?')


new_dice = reroll_selected(my_dice, indices_to_reroll)

print(new_dice)