from dataclasses import dataclass
import random
import numpy as np
from utils import compress, merge, reverse, transp, is_move_available, print_move_not_possible, \
    minimax_for_clean_wrapper


@dataclass
class Node:
    move: str
    score: int
    score_after_next_move: int


class Grid:
    available_moves = ["left", "right", "up", "down"]
    increase_free_tiles = 0
    counter = 0
    depth = 4

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

        # self.board[0][0] = 16
        # self.board[0][1] = 2
        # self.board[0][2] = 4
        # self.board[0][3] = 2
        #
        # self.board[1][0] = 4
        # self.board[1][1] = 32
        # self.board[1][2] = 128
        # self.board[1][3] = 4
        #
        # self.board[2][0] = 64
        # self.board[2][1] = 16
        # self.board[2][2] = 8
        # self.board[2][3] = 2
        #
        # self.board[3][0] = 2
        # self.board[3][1] = 8
        # self.board[3][2] = 2
        # self.board[3][3] = 0

        # self.board[1][0] = 4
        # self.board[2][0] = 8
        # self.board[3][0] = 8
        # self.board[3][1] = 4

        self.board[0][3] = 4
        self.board[0][2] = 4
        #
        #
        # self.board[0][0] = 2
        # self.board[0][1] = 4
        # self.board[1][1] = 2

        self.display()

    def new_values(self, only_two):
        if self.get_free_tiles() == 0:
            return

        ij = [random.randint(0, 3), random.randint(0, 3)]
        while self.board[ij[0]][ij[1]] != 0:
            ij = [random.randint(0, 3), random.randint(0, 3)]

        if only_two:
            self.board[ij[0]][ij[1]] = 2
        else:
            self.board[ij[0]][ij[1]] = random.choices([2, 4], [0.9, 0.1])[0]

    def left(self, is_game_play, only_two):
        arr1 = self.board.copy()

        arr2 = compress(arr1)
        arr3, self.score = merge(arr2, self.score)
        self.board = compress(arr3)

        if is_game_play:
            self.new_values(only_two)

    ##        self.display()

    def right(self, is_game_play, only_two):
        arr1 = self.board.copy()

        arr2 = reverse(arr1)
        arr3 = compress(arr2)
        arr4, self.score = merge(arr3, self.score)
        arr5 = compress(arr4)
        self.board = reverse(arr5)

        if is_game_play:
            self.new_values(only_two)

    ##        self.display()

    def up(self, is_game_play, only_two):
        arr1 = self.board.copy()

        arr2 = transp(arr1)
        arr3 = compress(arr2)
        arr4, self.score = merge(arr3, self.score)
        arr5 = compress(arr4)
        self.board = transp(arr5)

        if is_game_play:
            self.new_values(only_two)

    ##        self.display()

    def down(self, is_game_play, only_two):
        arr1 = self.board.copy()

        arr2 = transp(arr1)
        arr3 = reverse(arr2)
        arr4 = compress(arr3)
        arr5, self.score = merge(arr4, self.score)
        arr6 = compress(arr5)
        arr7 = reverse(arr6)
        self.board = transp(arr7)

        if is_game_play:
            self.new_values(only_two)

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

    def move_tiles(self, move, is_game_play, only_two):
        if move == "left":
            self.left(is_game_play, only_two)
        elif move == "right":
            self.right(is_game_play, only_two)
        elif move == "up":
            self.up(is_game_play, only_two)
        elif move == "down":
            self.down(is_game_play, only_two)










    # def clean_up_board(self):
    #     ##is_move_available(self, move)
    #
    #     old_board = self.board
    #     old_score = self.score
    #     old_state = self.state
    #     best_move = "None"
    #     free_tiles = 0
    #     for move in self.available_moves:
    #         if not is_move_available(self, move):
    #             print_move_not_possible(move)
    #             continue
    #
    #         self.move_tiles(move, True)
    #         new_free_tiles = self.get_free_tiles()
    #         if new_free_tiles > free_tiles:
    #             best_move = move
    #             free_tiles = new_free_tiles
    #
    #         self.board = old_board
    #         self.score = old_score
    #         self.state = old_state
    #
    #
    #     if best_move == "None":
    #         best_move = self.get_best_possible_move(self.board)
    #         print("random")
    #
    #     if best_move == "None":
    #         print("Game lost!")
    #         exit()
    #     print(best_move, " from cleaned up")
    #     self.move_tiles(best_move, True)
    #     self.display()


    def ai_move(self):

        if self.get_free_tiles() < 4:
            minimax_for_clean_wrapper(self)
            self.counter = 0
            return
        else:
            self.counter += 1

        old_board = self.board
        old_score = self.score
        old_state = self.state

        #self.depth = 7

        if self.state == 100 :
            self.depth = 4
        elif self.state == 200:
            self.depth = 5
        elif self.state == 300:
            self.depth = 6
        # elif self.state == 400:
        #     self.depth = 4
        # elif self.state == 500:
        #     self.depth = 3




        best_move = Node("None", 0, 0)

        for move in self.available_moves:
            self.move_tiles(move, True, True)
            score_after_first_move = self.score - old_score

            leaf_node_val = []

            score_after_minimax = self.minimax(self.depth, self.board, leaf_node_val, 0)
            total_score = score_after_minimax + score_after_first_move

            percent = 0
            #



            if total_score > best_move.score:
                best_move = Node(move, total_score, score_after_first_move)
                # if best_move.score_after_next_move > score_after_first_move:
                #     percent = round(total_score / best_move.score, 1)
                #     difference_after_first_move = best_move.score_after_next_move - score_after_first_move
                #
                #     if percent > 1.1 and difference_after_first_move < 10:
                #         best_move = Node(move, total_score, score_after_first_move)
                #
                #     elif percent > 1.2 and difference_after_first_move < 20:
                #         best_move = Node(move, total_score, score_after_first_move)
                #
                #     elif percent > 1.3 and difference_after_first_move < 30:
                #         best_move = Node(move, total_score, score_after_first_move)
                # else:
                #     best_move = Node(move, total_score, score_after_first_move)

            elif total_score == best_move.score and score_after_first_move > best_move.score_after_next_move:
                best_move = Node(move, total_score, score_after_first_move)


            # elif total_score < best_move.score:
            #     if score_after_first_move > best_move.score_after_next_move:
            #         difference = best_move.score - total_score
            #         if difference < 10:
            #             best_move = Node(move, total_score, score_after_first_move)




            # print(move, " score after the first move ", score_after_first_move, " score minimax", score_after_minimax,
            #       " = ", total_score, " percent: ",  best_move.score, " / total = ", percent)

            self.board = old_board
            self.score = old_score
            self.state = old_state

        # if best_move.score < 100 and best_move.score_after_next_move < 9:
        #     minimax_for_clean_wrapper(self)
        #     return

        if best_move.move == "None":
            best_move.move = self.get_best_possible_move(self.board)
            print("Random!")

        if best_move.move == "None":
            print("Game lost!")
            exit()

        print(best_move.move)
        self.move_tiles(best_move.move, True, False)
        self.display()

## This method will be called when the minimax algorithm does not find any path
    def get_best_possible_move(self, board):
        old_board = self.board
        at_least_possible_move = "None"
        for move in self.available_moves:
            if not is_move_available(self, move):
                print_move_not_possible(move)
                continue

            self.board = board
            self.move_tiles(move, True, True)

            if self.is_next_move_available():
                self.board = old_board
                return move

            self.board = old_board
            at_least_possible_move = move

        return at_least_possible_move


## This method makes sure the added value(2 or 4) is close to 2s and 4s
    def is_next_move_available(self):
        size = 4
        for row in range(size - 1):
            for column in range(size):
                if self.board[row][column] == 2:
                    if self.board[row + 1][column] == 2 or self.board[row + 1][column] == 0:
                        return True

        for row in range(size):
            for column in range(size - 1):
                if self.board[row][column] == 2:
                    if self.board[row][column + 1] == 2 or self.board[row][column + 1] == 0:
                        return True





    def minimax(self, depth, board, leaf_values, score):
        if depth < 1:
            #leaf_values.append(self.score)
            leaf_values.append(score)
            return 0
        #self.score = score

        for move in self.available_moves:
            if is_move_available(self, move):
                self.board = board
                self.score = score
                self.move_tiles(move, True, True)
                self.minimax(depth - 1, self.board, leaf_values, self.score)

            else:
                self.minimax(0, self.board, leaf_values, score)


        return max(leaf_values)

    def get_free_tiles(self):
        size = 4
        counter = 16
        for row in range(size):
            for column in range(size):
                value = self.board[row][column]
                if value != 0:
                    counter -= 1
        #print("from free tiles ", counter)
        return counter

    def is_point_available(self, move):
        if move == "left" or move == "right":
            return self.is_row_matching()
        else:
            return self.is_column_matching()


g = Grid()

while str(input()) != "exit":
    for i in range(1000):
        g.ai_move()
        #minimax_for_clean_wrapper(g)
