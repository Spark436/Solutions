# Create an algorithm that creates the patterns seen in the red and black knights video seen in the explanation
# Make the algorithm visible so that the user can see the patterns that are created
# Create a chess board
# Create a spiral of numbers on the chess board
# step 1 generate variable possibilities from move1 and move2
# step 2 in place brick calculate all 8 threatened squares
# step 3 generate for each player a list with available squares
# step 4 remove the threatened squares from step 2, from the opponents list of available squares

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
        pass

    def find_free_square(self):
        pass

    def print(self):
        for row in self.board:
            for column in row:
                print(column, end=" ")
            print()


class Brick:
    def __init__(self, color, move1, move2):
        self.color = color
        self.moves = [
            (x * move1, y * move2)
            for x in (-1, 1)
            for y in (-1, 1)
        ] + [
            (x * move2, y * move1)
            for x in (-1, 1)
            for y in (-1, 1)
        ]

        self.available_squares = [x for x in range(200)]  # find max spiral value # generate list with list comprehension


        # move 1 = 1 move 2 = 2 8 possibilities:  1, 2  1, -2  -1, 2  -1, -2  2, 1  2, -1  -2, 1  -2, -1


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
# print(board.board[3][2])
board.print()
spiral2board, board2spiral = make_spiral_board_dict(200)
# print(spiral2board)
# print(spiral2board[5])
# print(board2spiral[(3, 4)])
# print(knight.moves)
# print(board2spiral)
print(knight.available_squares)
# print(board.x)
# print(board.y)

# class Knight:
