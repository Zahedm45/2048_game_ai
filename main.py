import random
import numpy as np
from utils import compress, merge, reverse, transp


class Grid:
    def __init__(self):
        self.state = 0
        self.board = np.zeros((4, 4), dtype=int)
        i_1 = [random.randint(0, 3), random.randint(0, 3)]
        i_2 = [random.randint(0, 3), random.randint(0, 3)]
        while i_2 == i_1:
            i_2 = [random.randint(0, 3), random.randint(0, 3)]
        self.board[i_1[0]][i_1[1]], self.board[i_2[0]][i_2[1]] = 2, 2
        self.display()

    def new_values(self):
        c = 0
        ij = [random.randint(0, 3), random.randint(0, 3)]
        while c < 2:
            while self.board[ij[0]][ij[1]] != 0:
                ij = [random.randint(0, 3), random.randint(0, 3)]
            self.board[ij[0]][ij[1]] = 2
            c += 1

    def left(self):
        arr1 = self.board.copy()

        arr2 = compress(arr1)
        arr3 = merge(arr2)
        self.board = compress(arr3)

        self.new_values()
        self.display()

    def right(self):
        arr1 = self.board.copy()

        arr2 = reverse(arr1)
        arr3 = compress(arr2)
        arr4 = merge(arr3)
        arr5 = compress(arr4)
        self.board = reverse(arr5)

        self.new_values()
        self.display()

    def up(self):
        arr1 = self.board.copy()

        arr2 = transp(arr1)
        arr3 = compress(arr2)
        arr4 = merge(arr3)
        arr5 = compress(arr4)
        self.board = transp(arr5)

        self.new_values()
        self.display()

    def down(self):
        arr1 = self.board.copy()

        arr2 = transp(arr1)
        arr3 = reverse(arr2)
        arr4 = compress(arr3)
        arr5 = merge(arr4)
        arr6 = compress(arr5)
        arr7 = reverse(arr6)
        self.board = transp(arr7)

        self.new_values()
        self.display()

    def display(self):
        print("-----------------------------------------")

        print("state: " + str(self.state))
        print("")
        for row in self.board:
            print(
                "{:<10s} {:<10s} {:<10s} {:<10s}".format(
                    str(row[0]) if row[0] != 0 else ".",
                    str(row[1]) if row[1] != 0 else ".",
                    str(row[2]) if row[2] != 0 else ".",
                    str(row[3]) if row[3] != 0 else ".",
                )
            )
        print("")
        self.state += 1


g = Grid()
