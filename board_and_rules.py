"""
Clase creada por chatgpt con el prompt:
Crea una clase para simular un juego de conecta 4. Esta debe de tener las mismas reglas de
victoria que en el juego original, colocar las fichas de abajo hacia arriba, revisar si las
filas y columnas son validas o están llenas y debe de devolver el tablero. 
"""

import numpy as np

class Connect4:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.board = np.zeros((rows, columns), dtype=int)

    def drop_piece(self, column, player):
        for row in range(self.rows):
            if self.board[row, column] == 0:
                self.board[row, column] = player
                return True
        return False

    def is_valid_location(self, column):
        return self.board[5, column] == 0

    def get_valid_columns(self):
        return [c for c in range(self.columns) if self.is_valid_location(c)]

    def print_board(self):
        print(np.flip(self.board, 0))

    def check_winner(self, player):
        # Horizontal
        for r in range(self.rows):
            for c in range(self.columns-3):
                if all(self.board[r, c+i] == player for i in range(4)):
                    return True

        # Vertical
        for c in range(self.columns):
            for r in range(self.rows-3):
                if all(self.board[r+i, c] == player for i in range(4)):
                    return True

        # Diagonal positiva
        for r in range(self.rows-3):
            for c in range(self.columns-3):
                if all(self.board[r+i, c+i] == player for i in range(4)):
                    return True

        # Diagonal negativa
        for r in range(3, self.rows):
            for c in range(self.columns-3):
                if all(self.board[r-i, c+i] == player for i in range(4)):
                    return True

        return False
    
    """HASTA AQUÍ LLEGÓ LO QUE ME DIÓ CHAT CON EL PROMPT"""