"""
Docstring for Untitled-1
"""
import random
import sys

def roll_dice(num_dice = 5):
    """Roll a specified number of dice."""
    return [random.randint(1, 6) for _ in range(num_dice)]

def get_dice_to_keep(dice):
    """Prompt the user for which dice to keep."""
    print(f"Current dice: {dice}")
    # Get input (e.g., "1 3 5" to keep the first, third, and fifth dice)
    user_input = input("Enter the indices (1-5) of the dice you want to keep, separated by spaces (or 'all'/'none'): ")

    if user_input.lower() == 'all':
        return [True] * 5
    elif user_input.lower() == 'none' or user_input.strip() == '':
        return [False] * 5

    # Process indices
    keep_status = [False] * 5
    try:
        # Convert 1-based index input to 0-based index
        indices_to_keep = [int(i) - 1 for i in user_input.split()]
        for index in indices_to_keep:
            if 0 <= index < 5:
                keep_status[index] = True
            else:
                print(f"Warning: Index {index + 1} is out of range. Skipping.")
    except ValueError:
        print("Invalid input format. Rerolling all dice by default.")
        return [False] * 5

    return keep_status

def handle_reroll(current_dice):
    """
    Docstring for handle_reroll
    
    :param current_dice: Description
    """
    keep_status = get_dice_to_keep(current_dice)

    new_dice = []
    for i in range(5):
        if keep_status[i]:
            new_dice.append(current_dice[i])
        else:
            new_dice.append(random.randint(1, 6))

    return new_dice


# Initial setup
r_to_r = input('ready to roll? Y or N:')
dice = roll_dice(5)
# Use a boolean list to track kept dice: False means reroll, True means keep
get_dice_to_keep(dice)

print(f"Initial roll: {dice}")
print(f"Keep status: {keep_status}") # Initially all False

print(f"\nUpdated keep status: {keep_status}")
sys.exit()
# Logic for rerolling:
new_dice = []
for i in range(5):
    if keep_status[i]:
        new_dice.append(dice[i]) # Keep the old die value
    else:
        new_dice.append(random.randint(1, 6)) # Roll a new die

dice = new_dice
print(f"Dice after reroll (keeping index 0 and 2): {dice}")
# EOF# Usage example:
# current_dice = [2, 4, 1, 6, 3]
# current_dice = handle_reroll(current_dice)
# print(f"New dice values: {current_dice}")
 # EOF
