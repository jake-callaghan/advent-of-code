import copy
import math


class Vector:
    """Defines a 2-coordinate vector (i,j) with standard operations and an optional value to be stored there"""
    def __init__(self, i: int, j: int, value=None):
        self._i = i
        self._j = j
        self._value = value

    @property
    def i(self):
        return self._i

    @property
    def j(self):
        return self._j

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @value.deleter
    def value(self):
        del self._value

    def __len__(self):
        """Manhattan distance from origin"""
        return abs(self.i) + abs(self.j)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.i + other.i, self.j + other.j, self.value)
        if isinstance(other, tuple):
            return Vector(self.i + other[0], self.j + other[1], self.value)
        return self

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.i - other.i, self.j - other.j, self.value)
        if isinstance(other, tuple):
            return Vector(self.i - other[0], self.j - other[1], self.value)
        return self

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.i * other.i, self.j * other.j, self.value)
        if isinstance(other, tuple):
            return Vector(self.i * other[0], self.j * other[1], self.value)
        if isinstance(other, int):
            return Vector(self.i * other, self.j * other, self.value)
        return self

    def __str__(self):
        return f"({self.i},{self.j}){'' if self.value is None else ' -> ' + str(self.value)}"

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.i == other.i and self.j == other.j and self.value == other.value
        if isinstance(other, tuple):
            return self.i == other[0] and self.j == other[1]
        return False

    @staticmethod
    def parse(x):
        """Parse some standard input strings into a vector"""
        match x.upper():
            case 'UP' | 'U':
                return Vector(0, 1)
            case 'DOWN' | 'D':
                return Vector(0, -1)
            case 'LEFT' | 'L':
                return Vector(-1, 0)
            case 'RIGHT' | 'R':
                return Vector(1, 0)
        return None

    def manhattan_distance(self, other):
        return abs(self.i - other.i) + abs(self.j - other.j)

    def real_distance(self, other):
        return math.sqrt((self.i - other.i) ** 2 + (self.j - other.j) ** 2)

    def __copy__(self):
        return Vector(self.i, self.j, self.value)

    def __contains__(self, item):
        return self.value == item

    def copy(self):
        return copy.copy(self)

    def __hash__(self):
        return hash(self.__str__())

    def moore_neighborhood(self):
        return [Vector(self.i+di, self.j+dj) for di, dj in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]]
