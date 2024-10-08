board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")

def check_win(player):
    return (
        (board[0] == board[1] == board[2] == player) or  
        (board[3] == board[4] == board[5] == player) or  
        (board[6] == board[7] == board[8] == player) or  
        (board[0] == board[3] == board[6] == player) or  
        (board[1] == board[4] == board[7] == player) or  
        (board[2] == board[5] == board[8] == player) or  
        (board[0] == board[4] == board[8] == player) or  
        (board[2] == board[4] == board[6] == player)    
    )

def tic_tac_toe():
    current_player = "X"
    
    for _ in range(9):  # Only 9 possible moves
        print_board()
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        board[move] = current_player
        
        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            return
        
        current_player = "O" if current_player == "X" else "X"
    
    print_board()
    print("It's a draw!")

tic_tac_toe()
