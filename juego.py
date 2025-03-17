import time
from board_and_rules import Connect4, minimax


def play_game():
    game = Connect4()
    turn = 1

    mode = input(
        "Elige el modo de juego: 1 (Humano vs IA) o 2 (IA vs IA - Sin poda vs Con poda): "
    )
    human_players = mode == "1"

    time_ai_1 = 0
    time_ai_2 = 0

    while True:
        game.print_board()
        player = 1 if turn % 2 != 0 else 2

        if human_players and player == 1:
            try:
                column = int(input(f"Jugador {player}, elige una columna (1-7): ")) - 1
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
        else:
            use_alpha_beta = player == 2
            start_time = time.time()
            column, _ = minimax(
                game, 4, -float("inf"), float("inf"), True, player, use_alpha_beta
            )
            timing = time.time() - start_time

            if player == 1:
                time_ai_1 += timing
            else:
                time_ai_2 += timing

            print(
                "----------------------------------------player: ",
                player,
                "esta usando alpha_beta?: ",
                use_alpha_beta,
                "tiempo tomado: ",
                round(timing, 4),
                "s ----------------------------------------",
            )
            game.drop_piece(column, player)
            print(
                f"Jugador {player} (AI{' con poda' if use_alpha_beta else ' sin poda'}) elige la columna: {column+1}"
            )

        if game.check_winner(player):
            game.print_board()
            print(f"¡Jugador {player} ha ganado!")
            break

        if len(game.get_valid_columns()) == 0:
            game.print_board()
            print("¡Empate!")
            break

        turn += 1

    print("\nTiempo total de ejecución:")
    print(f"AI 1 (sin poda): {round(time_ai_1, 4)} s")
    print(f"AI 2 (con poda): {round(time_ai_2, 4)} s")


if __name__ == "__main__":
    play_game()
