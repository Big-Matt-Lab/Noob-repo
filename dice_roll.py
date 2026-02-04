"""
Docstring for Untitled-1
"""

import random
# import sys # sys is not needed if we manage game flow with loops


def roll_dice(num_dice=5):
    """Roll a specified number of dice and returns a list of results."""
    return [random.randint(1, 6) for _ in range(num_dice)]


def get_dice_to_keep(dice):
    """Prompt the user for which dice to keep."""
    print(f"Current dice: {dice}")
    # Get input (e.g., "1 3 5" to keep the first, third, and fifth dice)
    user_input = input(
        "Enter the indices (1-5) of the dice you want to keep, separated by spaces (or 'all'/'none'): "
    )

    if user_input.lower() == "all":
        return [True] * 5
    elif user_input.lower() == "none" or user_input.strip() == "":
        print("No dice kept. All will be rerolled.")
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


def reroll_dice(current_dice, keep_status):
    """
    Rerolls dice based on the keep_status.
    Dice marked True in keep_status are kept, others are rerolled.
    """
    new_dice = []
    for i, die_value in enumerate(current_dice):
        if keep_status[i]: # Check the keep_status for the current index
            new_dice.append(die_value)
        else:
            new_dice.append(random.randint(1, 6))
    return new_dice


# Main game loop
def main():
    """
    Docstring for play_dice_game
    """
    print("Welcome to the Dice Roller!")

    r_to_r = input("Ready to roll? Y or N: ").upper()
    if r_to_r != "Y":
        print("Maybe next time!")
        return

    dice = roll_dice(5)
    print(f"Initial roll: {dice}")

    # Allow for a fixed number of rerolls (e.g., 2 rerolls after the initial roll)
    num_rerolls_allowed = 2
    for roll_count in range(num_rerolls_allowed):
        print(f"\n--- Reroll {roll_count + 1} of {num_rerolls_allowed} ---")
        keep_status = get_dice_to_keep(dice)

        # If all dice are kept, no need to reroll. Break the reroll loop.
        if all(keep_status):
            print("All dice kept. No reroll performed.")
            break

        dice = reroll_dice(dice, keep_status)
        print(f"Dice after reroll: {dice}")

    print("\nFinal dice values:")
    print(dice)
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
