# Function to draw the board
def draw_board(board):
    print("     R   O   W")
    print("     1   2   3")
    print(f"C 1  {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("    ---+---+---")
    print(f"O 2  {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("    ---+---+---")
    print(f"L 3  {board[2][0]} | {board[2][1]} | {board[2][2]} ")

# Function to check for a winner
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(symbol == player for symbol in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] == player) or (board[0][2] == board[1][1] == board[2][0] == player):
        return True

    return False

# Function to evaluate the board state
def evaluate_board(board):
    if check_winner(board, 'O'):
        return 1  # AI ('O') wins
    elif check_winner(board, 'X'):
        return -1  # Player ('X') wins
    else:
        return 0  # Draw

# Function to get all possible moves
def get_possible_moves(board):
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                moves.append((row, col))
    return moves

# Minimax function to determine the best move
def minimax(board, depth, is_maximizing):
    score = evaluate_board(board)

    if score == 1 or score == -1:
        return score

    if len(get_possible_moves(board)) == 0:
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for move in get_possible_moves(board):
            row, col = move
            board[row][col] = 'O'
            score = minimax(board, depth + 1, False)
            board[row][col] = ' '

            best_score = max(score, best_score)

        return best_score
    else:
        best_score = float('inf')
        for move in get_possible_moves(board):
            row, col = move
            board[row][col] = 'X'
            score = minimax(board, depth + 1, True)
            board[row][col] = ' '

            best_score = min(score, best_score)

        return best_score

# Initialize the board
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

# Player 1: X
# Player 2: O
players = {'X': 'HUMAN PLAYER', 'O': 'AI'}

# Variable to alternate between players
current_player = 'X'

# Game loop
while True:
    # Draw the board
    draw_board(board)

    # Current player's turn
    print("\n++++++++++++++++++++")
    print(f"TURN OF {players[current_player]} ({current_player})")
    print("++++++++++++++++++++\n")

    if current_player == 'X':
        # Get the row and column selected by the player
        while True:
            row = int(input("Enter the row: "))
            column = int(input("Enter the column: "))

            # Check if the cell is empty
            if board[row - 1][column - 1] == ' ':
                break
            else:
                print("Invalid coordinates! The cell is already occupied. Try again.")

        # Mark the player's move as 'X'
        board[row - 1][column - 1] = 'X'
    else:
        # Get the best move for the AI using the minimax algorithm
        best_score = float('-inf')
        best_move = None

        for move in get_possible_moves(board):
            row, column = move
            board[row][column] = 'O'
            score = minimax(board, 0, False)
            board[row][column] = ' '

            if score > best_score:
                best_score = score
                best_move = move

        row, column = best_move
        board[row][column] = 'O'  # Mark the AI's move as 'O'
        print(f"The AI selects row {row + 1} and column {column + 1}")

    # Check for a winner
    if check_winner(board, current_player):
        # Draw the updated board
        draw_board(board)
        print(f"\n{players[current_player]} ({current_player}) has won!")
        break

    # Check for a draw
    if all(symbol != ' ' for row in board for symbol in row):
        # Draw the updated board
        draw_board(board)
        print("\nIt's a draw!")
        break

    # Switch players
    current_player = 'O' if current_player == 'X' else 'X'

