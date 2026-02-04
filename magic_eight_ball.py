"""
A simple Magic Eight Ball script that provides random answers to a question.
"""

import random

RESPONSES = [
    "It is certain.",
    "It is decidedly so.",
    "Reply hazy try again.",
    "Cannot predict now.",
    "Do not count on it.",
    "My sources say no.",
    "Outlook not so good.",
    "Signs point to yes.",
]


def question():
    """Prompts user to add a simple question"""
    # Combine the prompt and input into a single, more direct line
    return input("Ask your question of the Magic Eight Ball (type 'q' to quit): ").strip()


def response():
    """Selects and returns a random Magic 8-Ball response."""
    return random.choice(RESPONSES)


def main():
    """
    Main function to run the Magic 8-Ball game.
    It prompts a user question and prints a random response.
    """

    while True:
        user_question = question().lower()  # Normalize input for 'q' check (question() now strips)
        if user_question == "q":  # Check for quit immediately
            break

        # Only capitalize and print the question if the user didn't quit
        query = user_question.capitalize()
        eight_ball_answer = response()

        print(f"\nYou asked '{query}?'")  # Add a question mark for clarity
        print(eight_ball_answer)
        print()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()

# EOF
