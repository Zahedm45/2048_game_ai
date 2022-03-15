import random
import numpy as np
from utils import compress, merge, reverse, transp


class Grid:
    available_moves = ["left", "right", "up", "down"]

    # old_board = 0
    # old_score = 0
    # old_state = 0
    def __init__(self):
        self.score = 0
        self.state = 0
        self.board = np.zeros((4, 4), dtype=int)
        i_1 = [random.randint(0, 3), random.randint(0, 3)]
        i_2 = [random.randint(0, 3), random.randint(0, 3)]
        while i_2 == i_1:
            i_2 = [random.randint(0, 3), random.randint(0, 3)]

        ##        self.board[i_1[0]][i_1[1]], self.board[i_2[0]][i_2[1]] = 2, 2

        self.board[0][0] = 2
        self.board[0][1] = 256
        self.board[0][2] = 4
        self.board[0][3] = 2

        self.board[1][0] = 2
        self.board[1][1] = 64
        self.board[1][2] = 8
        self.board[1][3] = 2

        self.board[2][0] = 8
        self.board[2][1] = 512
        self.board[2][2] = 8
        self.board[2][3] = 2

        self.board[3][0] = 8
        self.board[3][1] = 4
        self.board[3][2] = 2
        self.board[3][3] = 4






        # self.board[1][0] = 4
        # self.board[2][0] = 8
        # self.board[3][0] = 8
        # self.board[3][1] = 4


        # self.board[0][3] = 4
        # self.board[0][2] = 4
        #
        #
        self.board[2][3] = 2
        self.board[3][3] = 4


        self.display()

    def new_values(self):
        print("new value")
        ij = [random.randint(0, 3), random.randint(0, 3)]
        while self.board[ij[0]][ij[1]] != 0:
            ij = [random.randint(0, 3), random.randint(0, 3)]
        self.board[ij[0]][ij[1]] = random.choices([2, 4], [0.9, 0.1])[0]

    def left(self, is_game_play):
        arr1 = self.board.copy()

        arr2 = compress(arr1)
        arr3, self.score = merge(arr2, self.score)
        self.board = compress(arr3)

        if is_game_play:
            self.new_values()


    ##        self.display()

    def right(self, is_game_play):
        arr1 = self.board.copy()

        arr2 = reverse(arr1)
        arr3 = compress(arr2)
        arr4, self.score = merge(arr3, self.score)
        arr5 = compress(arr4)
        self.board = reverse(arr5)

        if is_game_play:
            self.new_values()

    ##        self.display()

    def up(self, is_game_play):
        arr1 = self.board.copy()

        arr2 = transp(arr1)
        arr3 = compress(arr2)
        arr4, self.score = merge(arr3, self.score)
        arr5 = compress(arr4)
        self.board = transp(arr5)

        if is_game_play:
            self.new_values()

    ##        self.display()

    def down(self, is_game_play):
        arr1 = self.board.copy()

        arr2 = transp(arr1)
        arr3 = reverse(arr2)
        arr4 = compress(arr3)
        arr5, self.score = merge(arr4, self.score)
        arr6 = compress(arr5)
        arr7 = reverse(arr6)
        self.board = transp(arr7)

        if is_game_play:
            self.new_values()

    ##        self.display()

    def display(self):
        print("-----------------------------------------")
        print("State: " + str(self.state) + "       " + "Score: " + str(self.score))
        print("")
        for row in self.board:
            print(
                "{:<10s} {:<10s} {:<10s} {:<10s}".format(
                    *[str(r) if r != 0 else "." for r in row]
                )
            )

        self.state += 1

    def is_row_matching(self):
        size = 4

        for row in range(size):
            for column in range(size - 1):
                value = self.board[row][column]
                if value != 0 and value == self.board[row][column + 1]:
                    return True

        return False


    def is_column_matching(self):
        size = 4

        for row in range(size - 1):
            for column in range(size):
                value = self.board[row][column]
                if value != 0 and value == self.board[row + 1][column]:
                    return True

        return False


    def move_tiles(self, move, is_game_play):
        if move == "left":
            self.left(is_game_play)
        elif move == "right":
            self.right(is_game_play)
        elif move == "up":
            self.up(is_game_play)
        elif move == "down":
            self.down(is_game_play)

    def ai_move(self):
        old_board = self.board
        old_score = self.score
        old_state = self.state

        best_move = None
        best_score = self.score

        counter = 0

        for move in self.available_moves:
            self.move_tiles(move, False)
            score = self.minimax(2, self.board, self.score)

            if score > best_score:
                best_score = score
                best_move = move
            elif score == best_score:
                counter += 1

            self.board = old_board
            self.score = old_score
            self.state = old_state

        if counter == len(self.available_moves):
            best_move = random.choice(self.available_moves)
            print("random")

        print(best_move)
        self.move_tiles(best_move, True)
        self.display()

    def minimax(self, depth, board, score):

        if depth < 1:
            return score

        self.board = board
        self.score = score

        for move in self.available_moves:
            if move == "left" or move == "right":
                if self.is_row_matching():
                    self.move_tiles(move, False)
                    return self.minimax(depth - 1, self.board, self.score)
            else:
                if self.is_column_matching():
                    self.move_tiles(move, False)
                    return self.minimax(depth - 1, self.board, self.score)

        return score




g = Grid()

while str(input()) != "exit":
    # g.move_tiles(random.choice(g.available_moves))
    # g.display()
    g.ai_move()
   ## g.move_tiles("down", True)


# def is_row_matching(self, row, column):
#     size = int(self.board.size / len(self.board[0]))
#     if column == size - 1:
#         ##            print("last element")
#         return
#
#     value = self.board[row][column]
#     i = column + 1
#     while i < size:
#         temp = self.board[row][i]
#         if temp != 0:
#             if temp == value:
#                 print("matched")
#                 return True
#             else:
#                 ##                    print("break")
#                 break
#         i += 1
#
# def is_column_matching(self, row, column):
#     size = int(self.board.size / len(self.board[0]))
#     if row == size - 1:
#         ##            print("last element (column)")
#         return
#
#     value = self.board[row][column]
#     i = row + 1
#     while i < size:
#         temp = self.board[i][column]
#         if temp != 0:
#             if temp == value:
#                 print("matched(column)")
#                 return True
#             else:
#                 ##                    print("break(column)")
#                 return False
#         i += 1
#

