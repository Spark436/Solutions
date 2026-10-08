# Create an algorithm that creates the patterns seen in the red and black knights video seen in the explanation
# Make the algorithm visible so that the user can see the patterns that are created
# Create a chess board
# Create a spiral of numbers on the chess board
#
class Board:
    def __init__(self, size):
        # self.x = range(size)
        # self.y = range(size)
        self.board = []
        for x in range(size):
            columns = []
            for y in range(size):
                columns.append(0)
            self.board.append(columns)

    def place_brick(self, brick, x, y):
        # self.board[3][2] = "R"
        self.board[x][y] = brick.color

    def mark_threatened(self):


    def find_free_square(self):
        pass

    def print(self):
        for row in self.board:
            for column in row:
                print(column, end=" ")
            print()


class Brick:
    def __init__(self, name, move1, move2):
        self.color = "R"


def board_to_spiral(x, y):
    return s


def spiral_to_board(s):
    return x, y


def make_board_to_spiral_dict():
    return dict


def make_spiral_board_dict(n):
    spiral2board = {}
    board2spiral = {}

    x, y = 0, 0
    spiral2board[0] = (x, y)
    board2spiral[(x, y)] = 0

    dx, dy = 1, 0
    step_lenght = 1
    s = 1

    while s < n:
        for _ in range(2):
            for _ in range(step_lenght):
                if s >= n:
                    return spiral2board, board2spiral

                x += dx
                y += dy

                spiral2board[s] = (x, y)
                board2spiral[(x, y)] = s
                s += 1

            dx, dy = -dy, dx
            print(dx, dy)

        step_lenght += 1
                # 1: {1, 0},
                # 2: {1, 1},
                # 3: {0, 1},
                # 4: {-1, 1},
                # 5: {-1, 0}},
    return spiral2board, board2spiral


board = Board(4)
knight = Brick("Red knight", 1, 2)
board.place_brick(knight, 3, 2)
print(board.board[3][2])
board.print()
spiral2board, board2spiral = make_spiral_board_dict(15)
print(spiral2board)
print(board2spiral)

# print(board.x)
# print(board.y)

# class Knight:
