"""Opening Docstring
Rock, Paper, Scissors game"""

# start the game
# import random for computer choice
import random

# Constants for readability
ROCK = "\u270a"
PAPER = "\u270b"
SCISSORS = "\u270c"

# Dictionary maps user input keys to the display emojis
MOVES = {"r": ROCK, "p": PAPER, "s": SCISSORS}

# Tally variables
wins = 0
losses = 0
ties = 0

# Welcome message

print(f"Rock, Paper, Scissors Game\n{ROCK} {PAPER} {SCISSORS}")
while True:
    # generate computer choice
    comp_choice = random.choice(list(MOVES.values()))

    # players choice
    user_input = input("\nChoose (R)ock, (P)aper or (S)cissors:").lower().strip()
    if user_input and user_input[0] in MOVES:
        players_choice = MOVES[user_input[0]]
    else:
        print("Invalid entry. Please try R, P, or S.")
        continue

    # print the choices
    print(f"You chose {players_choice} and the computer chose {comp_choice}.")

    # evaluate the choices
    if players_choice == comp_choice:
        print(f"You both chose {comp_choice}. Draw!")
        ties += 1
    elif (players_choice == ROCK and comp_choice == SCISSORS) or \
        (players_choice == PAPER and comp_choice == ROCK) or \
        (players_choice == SCISSORS and comp_choice == PAPER):
        print("You win!")
        print("Congratulations!")
        wins += 1
    else:
        print("You lose!")
        print("Better luck next time!")
        losses += 1

    # play again
    if not input("Play again? Y or N: ").lower().startswith("y"):
        break
# End of loop
# Tally up the wins and losses
print(f"You won {wins} times.")
print(f"You lost {losses} times.")
print(f"You tied {ties} times.")
print("Thanks for playing!")
# EOF
