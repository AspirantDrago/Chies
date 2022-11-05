WHITE = 1
BLACK = 0


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = [[None] * 8 for _ in range(8)]

    def current_player_color(self):
        return self.color

    def corrent_coords(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char
