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
