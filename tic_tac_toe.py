game_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def view():
    print(f"{game_board[0]} | {game_board[1]} | {game_board[2]}")
    print("---------")
    print(f"{game_board[3]} | {game_board[4]} | {game_board[5]}")
    print("---------")
    print(f"{game_board[6]} | {game_board[7]} | {game_board[8]}")

def move(gamer):
    while True:
        position = input(f"Player {gamer}, enter a number from 1 to 9 to mark: ")
        if position in game_board:
            game_board[int(position) - 1] = gamer
            break
        else:
            print("Invalid move! Try again!!!!!!!!!.")

def check_win(gamer):
    possibilities = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for poss in possibilities:
        if game_board[poss[0]] == game_board[poss[1]] == game_board[poss[2]] == gamer:
            return True
    return False

def play():
    view()
    current_player = "X"
    
    for i in range(9):
        move(current_player)
        view()
        
        if check_win(current_player):
            print(f"Congratulations, {current_player} You have won!")
            break
        
        current_player = "O" if current_player == "X" else "X"
    else:
        print("It's a draw!!!!!!")

play()