""" An attempt to create a 'wordle' style game"""
import random
import sys
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

def load_words(filename):
    """Load words from a file relative to the script location."""
    file_path = Path(__file__).parent / filename
    try:
        content = file_path.read_text(encoding="utf-8")
        return [line.strip().lower() for line in content.splitlines() if line.strip()]
    except FileNotFoundError:
        return []

GAME_WORD_LIST = load_words('game_words.txt')
ALLOWED_WORD_LIST = set(load_words('allowed_words.txt'))

if not GAME_WORD_LIST:
    print("Error: game_words.txt not found or empty.")
    sys.exit(1)

# Ensure secret words are always valid guesses
ALLOWED_WORD_LIST.update(GAME_WORD_LIST)

MAX_GUESSES = 6 # Change Max guesses to whatever practical number you need
WORD_LENGTH = 5

class WordleApp:
    """
    Docstring for WordleApp
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Python Wordle")
        self.root.geometry("400x600")

        self.secret_word = ""
        self.guesses_count = 0
        self.current_guess_str = tk.StringVar()

        self.setup_ui()
        self.start_new_game()

    def setup_ui(self):
        # Title
        tk.Label(self.root, text="WORDLE", font=("Helvetica", 24, "bold")).pack(pady=10)

        # Grid Frame
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(pady=10)

        self.cells = []
        for row in range(MAX_GUESSES):
            row_cells = []
            for col in range(WORD_LENGTH):
                lbl = tk.Label(
                    self.grid_frame,
                    text="",
                    width=4,
                    height=2,
                    font=("Helvetica", 20, "bold"),
                    relief="solid",
                    borderwidth=1,
                    bg="white"
                )
                lbl.grid(row=row, column=col, padx=3, pady=3)
                row_cells.append(lbl)
            self.cells.append(row_cells)

        # Input Frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=20)

        self.entry = tk.Entry(input_frame, textvariable=self.current_guess_str, font=("Helvetica", 14), width=10)
        self.entry.pack(side=tk.LEFT, padx=5)
        self.entry.bind("<Return>", self.handle_guess)

        btn = tk.Button(input_frame, text="Guess", command=self.handle_guess)
        btn.pack(side=tk.LEFT, padx=5)

        # Message Label
        self.msg_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.msg_label.pack(pady=10)

        # Restart Button
        tk.Button(self.root, text="New Game", command=self.start_new_game).pack(pady=5)

    def start_new_game(self):
        """
        Docstring for start_new_game
        
        :param self: Description
        """
        self.secret_word = random.choice(GAME_WORD_LIST)
        self.guesses_count = 0
        self.current_guess_str.set("")
        self.entry.config(state="normal")
        self.entry.focus_set()
        self.msg_label.config(text=f"Guess the {WORD_LENGTH}-letter word!", fg="black")

        # Reset grid
        for row in range(MAX_GUESSES):
            for col in range(WORD_LENGTH):
                self.cells[row][col].config(text="", bg="white")

    def handle_guess(self, event=None):
        """
        Docstring for handle_guess
        
        :param self: Description
        :param event: Description
        """
        guess = self.current_guess_str.get().strip().lower()

        if self.guesses_count >= MAX_GUESSES:
            return

        if len(guess) != WORD_LENGTH:
            self.msg_label.config(text=f"Word must be {WORD_LENGTH} letters.", fg="red")
            return

        if not guess.isalpha():
            self.msg_label.config(text="Letters only please.", fg="red")
            return

        if guess not in ALLOWED_WORD_LIST:
            self.msg_label.config(text="Word not in list.", fg="red")
            return

        # Valid guess
        self.msg_label.config(text="")
        self.update_grid(guess)
        self.guesses_count += 1
        self.current_guess_str.set("")

        if guess == self.secret_word:
            self.msg_label.config(text="You Won! \U0001F389", fg="green")
            self.entry.config(state="disabled")
            messagebox.showinfo("Winner", "Congratulations! You guessed the word!")
        elif self.guesses_count >= MAX_GUESSES:
            self.msg_label.config(text=f"Game Over. Word was: {self.secret_word.upper()}", fg="red")
            self.entry.config(state="disabled")
            messagebox.showinfo("Game Over", f"The word was {self.secret_word.upper()}")


    def update_grid(self, guess):
        """
        Docstring for update_grid
        
        :param self: Description
        :param guess: Description
        """
        row = self.guesses_count

        # Logic for colors
        # First pass: Correct (Green)
        # Second pass: Present (Yellow)

        secret_list = list(self.secret_word)
        guess_list = list(guess)
        colors = ["#787c7e"] * WORD_LENGTH # Default Grey

        # Pass 1: Greens
        for i in range(WORD_LENGTH):
            self.cells[row][i].config(text=guess_list[i].upper())
            if guess_list[i] == secret_list[i]:
                colors[i] = "#6aaa64" # Green
                secret_list[i] = None # Mark as used
                guess_list[i] = None # Mark as handled

        # Pass 2: Yellows
        for i in range(WORD_LENGTH):
            if guess_list[i] is not None: # If not already green
                if guess_list[i] in secret_list:
                    colors[i] = "#c9b458" # Yellow
                    secret_list[secret_list.index(guess_list[i])] = None # Mark first occurrence

        # Apply colors
        for i in range(WORD_LENGTH):
            self.cells[row][i].config(bg=colors[i], fg="white")


if __name__ == "__main__":
    root = tk.Tk()
    app = WordleApp(root)
    root.mainloop()

# EOF
