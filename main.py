WHITE = 1
BLACK = 0


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = [[None] * 8 for _ in range(8)]

    @property
    def current_player_color(self):
        return self.color

    @property
    def current_player_string(self):
        if self.color == WHITE:
            return 'Ход белых'
        return 'Ход черных'

    def corrent_coords(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char

    def __str__(self):
        line = '   +----+----+----+----+----+----+----+----+'
        result = [line]
        for row in range(7, -1, -1):
            result.append(f' {row} | {" | ".join(self.cell(row, col) for col in range(8))} |')
            result.append(line)
        result.append('      ' + '    '.join(map(str, range(8))))
        return '\n'.join(result)

    @staticmethod
    def help():
        return '''Команды:
    exit                                -- выход
    move <row> <col> <row1> <col1>      -- ход из клетки (row, col)
                                           в клетку (row1, col1)'''




def main():
    board = Board()
    while True:
        print(board)
        print(board.help())



if __name__ == '__main__':
    main()
