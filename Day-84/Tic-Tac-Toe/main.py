from board import display_board
from check_winner import check_winner

board = [" "] * 9

complete_game = True

while complete_game:
    x_game = True
    o_game = True

    while x_game:
        x = int(input(f"PLAYER X : Enter the position u wanna enter (1-9): "))
        if board[x - 1] == " ":
            board[x - 1] = "X"
            display_board(board)

            if check_winner(board) == "X":
                print("Player 'X' wins")
                complete_game = False
                o_game = False

            x_game = False
        else:
            print("Position is already occupied!")

    while o_game:
        o = int(input(f"PLAYER O : Enter the position u wanna enter (1-9): "))
        if board[o - 1] == " ":
            board[o - 1] = "O"
            display_board(board)
            if check_winner(board) == "O":
                print("Player 'O' wins")
                complete_game = False
                x_game = False

            o_game = False
        else:
            print("Position is already occupied!")
