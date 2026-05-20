node_count = 0

def minimax(game, depth, alpha, beta, is_maximizing):

    global node_count
    node_count += 1

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

            score = minimax(game, depth + 1, alpha, beta, False)

            game.board[move] = " "

            best_score = max(best_score, score)

            alpha = max(alpha, best_score)

            # PRUNING
            if beta <= alpha:
                break

        return best_score

    # Human turn (MIN)
    else:

        best_score = float("inf")

        for move in game.available_moves():

            game.board[move] = "X"

            score = minimax(game, depth + 1, alpha, beta, True)

            game.board[move] = " "

            best_score = min(best_score, score)

            beta = min(beta, best_score)

            # PRUNING
            if beta <= alpha:
                break

        return best_score


def best_move(game):

    global node_count
    node_count = 0

    best_score = -float("inf")
    move_choice = None

    for move in game.available_moves():

        game.board[move] = "O"

        score = minimax(game, 0, -float("inf"), float("inf"), False)

        game.board[move] = " "

        if score > best_score:
            best_score = score
            move_choice = move

    print(f"Nodes searched: {node_count}")

    return move_choice