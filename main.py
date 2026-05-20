from game import TicTacToe
from minimax import best_move

game = TicTacToe()

while True:

    # Human turn
    game.print_board()

    move = int(input("Enter your move (0-8): "))

    if move not in game.available_moves():
        print("Invalid move!")
        continue

    game.make_move(move, "X")

    if game.check_winner("X"):
        game.print_board()
        print("You win!")
        break

    if game.is_draw():
        game.print_board()
        print("It's a draw!")
        break

    # AI turn
    ai_move = best_move(game)

    game.make_move(ai_move, "O")

    print(f"AI chooses position {ai_move}")

    if game.check_winner("O"):
        game.print_board()
        print("AI wins!")
        break

    if game.is_draw():
        game.print_board()
        print("It's a draw!")
        break