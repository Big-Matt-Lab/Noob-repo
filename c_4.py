"""Connect Four Game Construction"""

# --- Constants ---
ROWS = 6
COLS = 7
EMPTY_SLOT = " "


def create_board():
    """Creates a data structure for the game board."""
    # Using a list of lists to represent the board
    # We'll have ROWS number of lists, and each list will have COLS number of EMPTY_SLOTs
    return [[EMPTY_SLOT for _ in range(COLS)] for _ in range(ROWS)]


def print_board(board):
    """Prints the board to the console based on the current board state."""
    # Print header
    header = "  " + "   ".join(str(i + 1) for i in range(COLS))
    print(header)

    # Print board rows
    row_separator = " +" + "---+" * COLS
    print(row_separator)

    for r in range(ROWS):
        # Each row is built dynamically by joining the pieces from the board data
        row_str = " | " + " | ".join(board[r][c] for c in range(COLS)) + " |"
        print(row_str)
        print(row_separator)


# --- Main Game ---
if __name__ == "__main__":
    game_board = create_board()
    print_board(game_board)
