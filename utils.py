import numpy as np


def compress(mat):
    new_mat = np.zeros((4, 4), dtype=int)
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                pos += 1
    return new_mat


def merge(mat, new_score):
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] += mat[i][j]
                new_score += mat[i][j]
                mat[i][j + 1] = 0
    return (np.array(mat), new_score)


def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3 - j])
    return np.array(new_mat)


def transp(mat):
    new_mat = np.zeros((4, 4), dtype=int)
    for i in range(4):
        for j in range(4):
            new_mat[i][j] = mat[j][i]
    return np.array(new_mat)



def is_move_available(self, move):
    size = 4
    if move == "left":
        if self.is_row_matching():
            return True
        else:
            for row in range(size):
                for column in range(size - 1):
                    val = self.board[row][column]
                    if val == 0 and self.board[row][column + 1] != 0:
                        return True
            return False

    elif move == "right":
        if self.is_row_matching():
            return True
        else:
            for row in range(size):
                for column in range(size - 1):
                    val = self.board[row][column]
                    if val != 0 and self.board[row][column + 1] == 0:
                        return True

            return False

    elif move == "up":
        if self.is_column_matching():
            return True
        else:
            for row in range(size - 1):
                for column in range(size):
                    val = self.board[row][column]
                    if val == 0 and self.board[row + 1][column] != 0:
                        return True
            return False

    elif move == "down":
        if self.is_column_matching():
            return True
        else:
            for row in range(size - 1):
                for column in range(size):
                    val = self.board[row][column]
                    if val != 0 and self.board[row + 1][column] == 0:
                        return True
            return False
    else:
        return False


def print_move_not_possible(move):
    print("Move: ", move, " is not possible!")