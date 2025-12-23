

import random
import sys
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

def parse_hand(hand_string):
    """Converts a comma-separated string of card ranks into a sorted list of integers."""
    # Split the string by commas and convert each element to an integer
    try:
        ranks = [int(rank.strip()) for rank in hand_string.split(',')]
        # Sort the ranks, which makes checking for straights/pairs easier
        ranks.sort()
        return ranks
    except ValueError:
        return "Invalid input. Please enter only numbers separated by commas."

my_dice = roll_dice(5)

print(my_dice)

dice_to_reroll_str = input('Enter the dice positions to reroll seperated by a spacee.g., 1 3 5): ')

indices_to_reroll = []
try:
    # Convert space-separated string of numbers to a list of 0-based integers
    indices_to_reroll = [int(i) - 1 for i in dice_to_reroll_str.split()]
except ValueError:
    print("Invalid input. Please enter only numbers separated by spaces.")

new_dice = reroll_selected(my_dice, indices_to_reroll)

print(new_dice)
# Some possible code samples for further development
#
#
#
#
#
sys.exit()








def check_pairs_sets(ranks):
    """Checks for pairs, three of a kind, and four of a kind."""
    counts = Counter(ranks)
    pairs = sum(1 for count in counts.values() if count == 2)
    three_of_a_kind = sum(1 for count in counts.values() if count == 3)
    four_of_a_kind = sum(1 for count in counts.values() if count == 4)

    if four_of_a_kind:
        return "Four of a Kind"
    elif three_of_a_kind and pairs:
        return "Full House"
    elif three_of_a_kind:
        return "Three of a Kind"
    elif pairs == 2:
        return "Two Pair"
    elif pairs == 1:
        return "One Pair"
    else:
        return "No pairs or sets"

def check_straight(ranks):
    """Checks if the hand is a straight (consecutive ranks)."""
    # Use a set to remove duplicates, then sort
    unique_ranks = sorted(list(set(ranks)))
    if len(unique_ranks) < 5: # A straight requires 5 unique cards
        return False

    # Check for a standard 5-card straight
    if len(unique_ranks) == 5 and (unique_ranks[-1] - unique_ranks[0] == 4):
        return True

    # Check for the A-5 straight (Ace, 2, 3, 4, 5) by treating Ace as 1
    low_ace_ranks = sorted(list(set([1 if r == 14 else r for r in ranks])))
    if len(low_ace_ranks) == 5 and (low_ace_ranks[-1] - low_ace_ranks[0] == 4):
        return True

    return False

# Example of using the evaluation functions:
hand1 = parse_hand("2, 2, 3, 4, 5")
hand2 = parse_hand("10, 11, 12, 13, 14")
hand3 = parse_hand("5, 7, 5, 8, 8")

print(f"Hand 1 ({hand1}): {check_pairs_sets(hand1)}, Straight: {check_straight(hand1)}")
print(f"Hand 2 ({hand2}): {check_pairs_sets(hand2)}, Straight: {check_straight(hand2)}")
print(f"Hand 3 ({hand3}): {check_pairs_sets(hand3)}, Straight: {check_straight(hand3)}")

