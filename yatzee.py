"""
Docstring for Yatzee sim
"""
import random
from collections import Counter

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

def check_pairs_sets(ranks):
    """Checks for pairs, three of a kind, and four of a kind."""
    counts = Counter(ranks)
    pairs = sum(1 for count in counts.values() if count == 2)
    three_of_a_kind = sum(1 for count in counts.values() if count == 3)
    four_of_a_kind = sum(1 for count in counts.values() if count == 4)
    yatzee = sum(1 for count in counts.values() if count == 5)

    if yatzee:
        return "Yatzee"
    if four_of_a_kind:
        return "Four of a Kind"
    if three_of_a_kind and pairs:
        return "Full House"
    if three_of_a_kind:
        return "Three of a Kind"
    if pairs == 2:
        return "Two Pair"
    if pairs == 1:
        return "One Pair"
    else:
        return "No pairs or sets"

def check_straight(my_dice):
    """Checks if the hand is a straight (consecutive ranks)."""
    # Use a set to remove duplicates, then sort
    unique_ranks = sorted(list(set(my_dice)))
    if len(unique_ranks) < 5: # A straight requires 5 unique cards
        return "No straight"

    # Check for a standard 5-card straight
    if len(unique_ranks) == 5 and (unique_ranks[-1] - unique_ranks[0] == 4):
        return "5 card straight"

    return "No straight"

my_dice = roll_dice(5)
my_dice.sort()
print(my_dice)
print(check_pairs_sets(my_dice))
print(check_straight(my_dice))

dice_to_reroll_str = input('Enter the dice positions to reroll separated by a spacee.g., 1 3 5): ')

indices_to_reroll = []
try:
    # Convert space-separated string of numbers to a list of 0-based integers
    indices_to_reroll = [int(i) - 1 for i in dice_to_reroll_str.split()]
except ValueError:
    print("Invalid input. Please enter only numbers separated by spaces.")

my_dice = reroll_selected(my_dice, indices_to_reroll)

my_dice.sort()
print(my_dice)
print(check_pairs_sets(my_dice))
print(check_straight(my_dice))

# EOF
