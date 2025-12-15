"""Opening Docstring
Rock, Paper, Scissors game"""

# emoji's U+270A,B,C
# start the game
# import random for computer choice
import random

# set tally variables
win = 0
loss = 0
ties = 0
again = True
while again:

    # generate computer choice
    comp_choice = random.choice(["rock", "paper", "scissors"])
    if comp_choice[0] == "r":
        comp_choice = '\u270A'
    elif comp_choice[0] == "p":
        comp_choice = '\u270B'
    elif comp_choice[0] == "s":
        comp_choice = '\u270C'

    # players choice
    players_choice = input("Choose Rock, Paper or Scissors(R,P,S):").lower()
    if players_choice == "r":
        players_choice = '\u270A'
    elif players_choice == "p":
        players_choice = '\u270B'
    elif players_choice == "s":
        players_choice = '\u270C'
    else:
        print("Invalid entry. Please try again.")
        continue

    # print the choices
    print(f"You chose {players_choice} and the computer chose {comp_choice}.")

    # evaluate the choices
    if players_choice == "\u270A" and comp_choice == "\u270C":
        print("You win!")
        print("Good choice!")
        win += 1
    elif players_choice == "\u270B" and comp_choice == "\u270A":
        print("You win!")
        print("Try again!")
        win += 1
    elif players_choice == "\u270C" and comp_choice == "\u270B":
        print("You win!")
        win += 1
    elif players_choice == comp_choice:
        print(f"You both chose {comp_choice}. Draw!")
        ties += 1
    else:
        print("You lose!")
        print("Better luck next time!")
        loss += 1

    # play again
    play_again = input("Play again? Y or N:").lower()
    if play_again == "y":
        again = True
    else:
        break
# End of loop
# Tally up the wins and losses
print(f"You won {win} times.")
print(f"You lost {loss} times.")
print(f"You tied {ties} times.")
print("Thanks for playing!")
# EOF
