def check_winner(board):
    winning_combinations = [
        # r
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        # c
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        # d
        (0, 4, 8),
        (2, 4, 6),
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    return None
