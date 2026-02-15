""" A Connect Four game"""
import random
import tkinter as tk

# Define Game Class ConnectFour
# Add methods
    # init
    # game setup
    # user input
    # row/column restrictions for token placement
    # four in a row check
    # play again/ new game

ROWS = 6
COLS = 7


class ConnectFourApp:
    """
    Connect Four Game Application
    """
    def __init__(self, root):
        """"""
        self.root = root
        self.root.title("Connect Four")
        self.root.geometry("600x600")

        self.turn = 'X'
        self.board = [['' for _ in range(COLS)] for _ in range(ROWS)]
        self.game_active = True

        self.setup_ui()

    def setup_ui(self):
        """Set up the game UI with a grid."""
        tk.Label(self.root, text="CONNECT FOUR", font=("Helvetica", 24, "bold")).pack(pady=10)

        # Grid Frame
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(pady=10)

        self.cells = []
        for row in range(ROWS):
            row_cells = []
            for col in range(COLS):
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
                lbl.bind("<Button-1>", lambda event, c=col: self.handle_click(c))
                row_cells.append(lbl)
            self.cells.append(row_cells)

        self.status_label = tk.Label(self.root, text=f"Player {self.turn}'s Turn", font=("Helvetica", 16))
        self.status_label.pack(pady=10)

        tk.Button(self.root, text="Play Again", command=self.reset_game).pack(pady=5)

    def reset_game(self):
        """Reset the game board for a new game."""
        self.game_active = True
        self.turn = 'X'
        self.board = [['' for _ in range(COLS)] for _ in range(ROWS)]

        for row in range(ROWS):
            for col in range(COLS):
                self.cells[row][col].config(text="", bg="white")

        self.status_label.config(text=f"Player {self.turn}'s Turn", fg="black", font=("Helvetica", 16))

    def handle_click(self, col):
        """Handle a click on a column (Player X)."""
        if not self.game_active or self.turn != 'X':
            return

        if self.make_move(col):
            if self.game_active:
                self.root.after(500, self.computer_move)

    def make_move(self, col):
        """Attempt to place a piece in the specified column."""
        for row in range(ROWS - 1, -1, -1):
            if self.board[row][col] == '':
                self.board[row][col] = self.turn
                self.update_cell(row, col)

                winning_cells = self.check_win(row, col)
                if winning_cells:
                    self.game_active = False
                    self.status_label.config(text=f"Player {self.turn} Wins!", fg="green", font=("Helvetica", 20, "bold"))
                    for r, c in winning_cells:
                        self.cells[r][c].config(bg="#90EE90")  # Light green highlight
                elif self.check_draw():
                    self.game_active = False
                    self.status_label.config(text="It's a Draw!", fg="orange", font=("Helvetica", 20, "bold"))
                else:
                    self.turn = 'O' if self.turn == 'X' else 'X'
                    self.status_label.config(text=f"Player {self.turn}'s Turn", fg="black")
                return True
        return False

    def computer_move(self):
        """Make a smart move for the computer."""
        if not self.game_active or self.turn != 'O':
            return

        valid_cols = [c for c in range(COLS) if self.board[0][c] == '']
        if not valid_cols:
            return

        # Check for winning move or blocking move
        for player in ['O', 'X']:
            for col in valid_cols:
                row = self.get_next_open_row(col)
                if row is None:
                    continue
                self.board[row][col] = player
                if self.check_win(row, col):
                    self.board[row][col] = ''  # Reset
                    self.make_move(col)
                    return
                self.board[row][col] = ''  # Reset

        col = random.choice(valid_cols)
        self.make_move(col)

    def get_next_open_row(self, col):
        """Return the next open row for a given column."""
        for row in range(ROWS - 1, -1, -1):
            if self.board[row][col] == '':
                return row
        return None

    def update_cell(self, row, col):
        """Update the UI for a cell."""
        player = self.board[row][col]
        color = "red" if player == 'X' else "yellow"
        self.cells[row][col].config(text=player, bg=color, fg="black")

    def check_win(self, row, col):
        """Check for 4 in a row starting from the placed piece."""
        player = self.board[row][col]
        # Directions: (row_delta, col_delta) -> Horizontal, Vertical, Diagonal /, Diagonal \
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

        for dr, dc in directions:
            winning_cells = [(row, col)]
            for step in [1, -1]:  # Check both positive and negative directions
                r, c = row + dr * step, col + dc * step
                while 0 <= r < ROWS and 0 <= c < COLS and self.board[r][c] == player:
                    winning_cells.append((r, c))
                    r += dr * step
                    c += dc * step

            if len(winning_cells) >= 4:
                return winning_cells
        return None

    def check_draw(self):
        """Check if the board is full."""
        return all(self.board[0][c] != '' for c in range(COLS))

def main():
    """ Main Game Call"""
    print("Starting Connect Four...")
    root = tk.Tk()
    app = ConnectFourApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
