from game import TicTacToe

game = TicTacToe()

current_player = "X"

while True:
    game.print_board()

    move = int(input(f"Player {current_player}, enter position (0-8): "))

    if move not in game.available_moves():
        print("Invalid move! Try again.")
        continue

    game.make_move(move, current_player)

    if game.check_winner(current_player):
        game.print_board()
        print(f"Player {current_player} wins!")
        break

    if game.is_draw():
        game.print_board()
        print("It's a draw!")
        break

    current_player = "O" if current_player == "X" else "X"