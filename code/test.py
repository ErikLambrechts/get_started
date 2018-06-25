import numpy as np

def render_char_matrix(m):
    print('\n'.join(["".join(r) for r in m]))

class Tile(object):
    def __init__(self):
        pass

    def render(self):
        pass
        if self.value == 0:
            return " "
        return self.value

class Wall(Tile):
    def render(self):
        return "#"

class Floor(Tile):
    def __init__(self, value = 0):
        self.value = value

    def render(self):
        return " "

class Grid(object):
    def __init__(self, n_rows, n_columns):
        self.n_rows = n_rows
        self.n_columns = n_columns

        self.tiles = []
        for i in range(n_rows):
            row = []
            for j in range(n_columns):
                value = np.random.randint(5)
                if i == 0 or j == 0:
                    row.append(Wall())
                elif i == n_rows - 1 or j == n_columns - 1:
                    row.append(Wall())
                # elif np.random.randint(8) == 0:
                #     row.append(Wall())
                else:
                    row.append(Floor(value))
            self.tiles.append(row)

    def render_list(self):
        output = []
        for r_ in self.tiles:
            output.append([t_.render() for t_ in r_])
        return output

    def render(self):
        render_char_matrix(self.render_list())

class Player(object):
    def __init__(self, x = 1, y = 1):
        self.x = x
        self.y = y

    def render(self):
        return "p"

class World(object):
    def __init__(self, grid, player = None):
        if player == None:
            player = Player()

        self.grid = grid
        self.player = player

    def render(self):
        out = self.grid.render_list()

        player_x = self.player.x
        player_y = self.player.y

        out[player_y][player_x] = self.player.render()

        render_char_matrix(out)

g = Grid(5, 6)


w = World(g)
w.render()
p = w.player
