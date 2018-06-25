import numpy as np
from colorama import Fore, Back, Style


class tile(object):
    def __init__(self, value = 0):
        self.value = value

    def render(self):
        if self.value == 0:
            return " "
        return self.value

class grid(object):
    def __init__(self, n_rows, n_columns):
        self.n_rows = n_rows
        self.n_columns = n_columns

        self.tiles = []
        for _ in range(n_rows):
            row = []
            for _ in range(n_columns):
                value = np.random.randint(5)
                row.append(tile(value))

            self.tiles.append(row)


    def render(self):
        for r_ in self.tiles:
            for t_ in r_:
                print(t_.render(), end="")
            print("")


g = grid(3, 4)

t = g.tiles[0][0]
g.render()
