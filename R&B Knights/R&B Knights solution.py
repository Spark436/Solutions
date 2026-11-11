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
        self.offset = size // 2

    def place_brick(self, friend_brick, evil_brick, x, y):
        # self.board[3][2] = "R"
        friend_brick.available_squares.remove(board2spiral[(x, y)]) # Remove the placed bricks square from both sides available squares
        evil_brick.available_squares.remove(board2spiral[(x, y)])
        self.board[x + self.offset][y + self.offset] = friend_brick.color
        # remove threatened squares from opponents available squares
        for delta_x, delta_y in friend_brick.moves:
            threatened_s = board2spiral[(x + delta_x, y + delta_y)]
            evil_brick.available_squares.remove(threatened_s)


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
            # print(dx, dy)

        step_lenght += 1
                # 1: {1, 0},
                # 2: {1, 1},
                # 3: {0, 1},
                # 4: {-1, 1},
                # 5: {-1, 0}},
    return spiral2board, board2spiral

board_size = 11
board = Board(board_size)
spiral2board, board2spiral = make_spiral_board_dict(board_size * board_size)
black_knight = Brick("B", 1, 2)
red_knight = Brick("R", 1, 2)
x, y = spiral2board[red_knight.available_squares[0]] # get the first available square for red # transform it to x, y and place a brick there
board.place_brick(red_knight, black_knight, x, y)
x, y = spiral2board[black_knight.available_squares[0]] # do the same for black
board.place_brick(black_knight, red_knight, x, y)
board.print()
# use the offset so the brick on 0, 0 is in the center of the board
while red_knight.available_squares or black_knight.available_squares: # set the placements of the red and black knights in a loop that ends when one side runs out of available squares
# print(board.board[3][2])
# print(spiral2board)
# print(spiral2board[5])
# print(board2spiral[(3, 4)])
# print(knight.moves)
# print(board2spiral)
print(black_knight.available_squares)
# print(board.x)
# print(board.y)

# class Knight:
