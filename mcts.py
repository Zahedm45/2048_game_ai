import numpy as np
from random import randint, random


def rm_zeros(the_list, val):
    return [value for value in the_list if value != val]


# new_game function
n = 4


def new_game(n):
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    return matrix
    # print(matrix)


# grid class: includes 1) getting game state, 2) moves, 3) score checking
class grid(object):
    def __init__(self):
        self.state = new_game(4)  # 4x4 zeros
        self.score = 0
        self.over = False
        self.win = False
        n = 4

    def get_empty_cells(self):
        for i in range(n):
            for j in range(n):
                if self.state[i][j] == 0:
                    yield i, j

    def get_same_cells(self):
        for i in range(n - 1):
            for j in range(n - 1):
                if (
                    self.state[i][j] == self.state[i + 1][j]
                    or self.state[i][j + 1] == self.state[i][j]
                ):
                    yield i, j

    def game_state(self):
        for i in range(n):
            for j in range(n):
                if self.state[i][j] == 2048:
                    self.win = True
        for i in range(n):
            for j in range(n):
                if self.state[i][j] == 0:
                    self.over = False
        cells = list(self.get_empty_cells())
        same_cells = list(self.get_same_cells())
        if not cells and not same_cells:
            self.over = True
        for i in range(n - 1):
            for j in range(n - 1):
                if (
                    self.state[i][j] == self.state[i + 1][j]
                    or self.state[i][j + 1] == self.state[i][j]
                ):
                    self.over = False

    def move(self, direction):
        out = np.asarray(self.state)  # new_game(4)
        addscore = 0
        if direction == "up":
            for i in range(n - 1):
                for j in range(n):
                    if self.state[i][j] == self.state[i + 1][j]:
                        out[i, j] = 2 * self.state[i][j]
                        out[i + 1, j] = 0
                        s = out[i, j]
                        addscore = addscore + s

            for i in range(n):
                out2 = out[out[:, i] != 0, i]
                if 4 - len(out2) > 0:
                    out[:, i] = np.pad(out2, [0, 4 - len(out2)], mode="constant")

        if direction == "down":
            for i in range(n - 1):
                for j in range(n):
                    if self.state[i][j] == self.state[i + 1][j]:
                        out[i, j] = 2 * self.state[i][j]
                        out[i + 1, j] = 0
                        s = out[i, j]
                        addscore = addscore + s

            for i in range(n):
                out2 = out[out[:, i] != 0, i]
                if 4 - len(out2) > 0:
                    out[:, i] = np.insert(out2, np.zeros(4 - len(out2)), 0, axis=0)

        if direction == "left":
            for i in range(n):
                for j in range(n - 1):
                    if self.state[i][j] == self.state[i][j + 1]:
                        out[i, j] = 2 * self.state[i][j]
                        out[i, j + 1] = 0
                        s = out[i, j]
                        addscore = addscore + s

            for i in range(n):
                out2 = out[i, out[i, :] != 0]
                if 4 - len(out2) > 0:
                    out[i, :] = np.pad(out2, [0, 4 - len(out2)], mode="constant")

        if direction == "right":
            for i in range(n):
                for j in range(n - 1):
                    if self.state[i][j] == self.state[i][j + 1]:
                        out[i, j] = 2 * self.state[i][j]
                        out[i, j + 1] = 0
                        s = out[i, j]
                        addscore = addscore + s

            for i in range(n):
                out2 = out[i, out[i, :] != 0]
                if 4 - len(out2) > 0:
                    out[i, :] = np.insert(out2, np.zeros(4 - len(out2)), 0, axis=0)

        # introduce new tile as part of the move:
        self.state = out
        self.score = self.score + addscore
        cells = list(self.get_empty_cells())
        if random() < 0.9:
            v = 2
        else:
            v = 4
        self.state[cells[randint(0, len(cells)) - 1]] = v


def mcts():
    while b0.over == False:
        show_grid(b0.score, b0.state)
        # time.sleep(0.2)
        b0.game_state()
        if b0.over == False:
            mcts_move = np.zeros(100)
            mcts_score = np.zeros(100)
            avg_mcts_score = np.zeros(4)
            for i in range(500):
                btest = copy.deepcopy(b0)
                try:
                    for d in range(10):
                        btest.game_state()
                        if btest.over == False:
                            try:
                                k = randint(0, 3)
                                if d == 0:
                                    mcts_move[i] = k
                                btest.move(options[k])
                            except:
                                try:
                                    l = [0, 1, 2, 3]
                                    l.remove(k)
                                    k = choice(l)
                                    btest.move(options[k])
                                except:
                                    fail_move = []
                        else:
                            mcts_score[i] = btest.score
                        mcts_score[i] = btest.score
                    del btest
                except:
                    fail_move = []
            for i in range(len(options)):
                avg_mcts_score[i] = np.mean(mcts_score[mcts_move == i])
            for i in range(len(options)):
                if avg_mcts_score[i] == max(avg_mcts_score):
                    b0.move(options[i])
