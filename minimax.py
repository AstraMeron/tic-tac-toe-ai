from game import TicTacToe

def minimax(game, is_maximizing):

    # Terminal states
    if game.check_winner("O"):
        return 1

    if game.check_winner("X"):
        return -1

    if game.is_draw():
        return 0

    # AI turn (MAX)
    if is_maximizing:
        best_score = -float("inf")

        for move in game.available_moves():
            game.board[move] = "O"

            score = minimax(game, False)

            game.board[move] = " "

            best_score = max(best_score, score)

        return best_score

    # Human turn (MIN)
    else:
        best_score = float("inf")

        for move in game.available_moves():
            game.board[move] = "X"

            score = minimax(game, True)

            game.board[move] = " "

            best_score = min(best_score, score)

        return best_score
    
    

def best_move(game):

    best_score = -float("inf")
    move_choice = None

    for move in game.available_moves():

        game.board[move] = "O"

        score = minimax(game, False)

        game.board[move] = " "

        if score > best_score:
            best_score = score
            move_choice = move

    return move_choice    