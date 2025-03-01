import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    
    return None

def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

def minimax(board, depth, is_max, alpha, beta):
    winner = check_winner(board)
    if winner == "X":
        return -10 + depth
    if winner == "O":
        return 10 - depth
    if not is_moves_left(board):
        return 0
    
    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = " "
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = " "
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human = "X"
    ai = "O"
    print("Tic-Tac-Toe: You are 'X', AI is 'O'")
    
    for turn in range(9):
        print_board(board)
        if turn % 2 == 0:
            while True:
                row, col = map(int, input("Enter your move (row and column: 0 1 2): ").split())
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    board[row][col] = human
                    break
                print("Invalid move, try again.")
        else:
            print("AI is making a move...")
            row, col = find_best_move(board)
            board[row][col] = ai
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} wins!")
            return
    
    print_board(board)
    print("It's a draw!")

tic_tac_toe()
