def display_board(board):

    for position in range(3):
        if position == 0:
            print(*board[:3], sep=" | ")
        elif position == 1:
            print("----------")
            print(*board[3:6], sep=" | ")
        else:
            print("----------")
            print(*board[6:9], sep=" | ")
