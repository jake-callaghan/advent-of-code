from core.vector import Vector


class Grid:
    """Represents a fixed-size 2D grid of Vectors"""
    def __init__(self, size=250, blank=None, points: [Vector] = None):
        self._size = size
        self._blank = blank
        self._grid = {}

        for row in range(0, size):
            self._grid[row] = {}
            for col in range(0, size):
                self._grid[row][col] = Vector(row, col, blank)

        if points is not None:
            for point in points:
                self._grid[point.i][point.j] = point

    @property
    def grid(self):
        return self._grid

    def _valid(self, row, col):
        return self._size > row >= 0 and self._size > col >= 0

    def get(self, row, col) -> Vector | None:
        if not self._valid(row, col):
            return None
        return self._grid[row][col]

    def __str__(self):
        s = ""
        for row in range(self._size, 0, -1):
            rowStr = ""
            for col in range(0, self._size):
                v = self.get(row, col)
                rowStr += '' if v is None else str(v.value)
            s += rowStr + '\n'
        return s

    def neighbors(self, row, col):
        """ returns the moore neighbourhood of vectors surrounding (row,col)"""
        if not self._valid(row, col):
            return []
        return [self.get(n.i, n.j) for n in self.get(row, col).moore_neighborhood()]

