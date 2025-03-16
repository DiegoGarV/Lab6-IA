from board_and_rules import Connect4


def play_game():
    game = Connect4()
    turn = 1

    while True:
        game.print_board()
        player = 1 if turn % 2 != 0 else 2

        try:
            column = int(input(f"Jugador {player}, elige una columna (1-7): "))
            column = column - 1
        except ValueError:
            print("Entrada inválida. Intenta nuevamente.")
            continue

        if column not in range(7):
            print("Columna fuera de rango. Intenta nuevamente.")
            continue

        if not game.is_valid_location(column):
            print("Columna llena. Intenta nuevamente.")
            continue

        game.drop_piece(column, player)

        if game.check_winner(player):
            game.print_board()
            print(f"¡Jugador {player} ha ganado!")
            break

        if len(game.get_valid_columns()) == 0:
            game.print_board()
            print("¡Empate!")
            break

        turn += 1


if __name__ == "__main__":
    play_game()