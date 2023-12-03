DIGITS = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def readfile(path) -> [str]:
    """Read in an input file and return a list of lines"""
    with open(path, 'r') as file:
        return [line.strip('\n') for line in file.readlines()]


def print_matrix(matrix, x_min=0, x_max=10, y_min=0, y_max=10, blank=' '):
    """Print a matrix of vectors within the grid defined by (x_min, y_min) to (x_max, y_max)"""
    for row in reversed(range(y_min, y_max+1)):
        print(f'{row}  ', end=blank)
        for col in range(x_min, x_max):
            found = False
            for vector in matrix:
                if vector.j == row and vector.i == col:
                    print(vector.value, end=blank)
                    found = True
                    break
            if not found:
                print(blank, end=blank)
        print()
    print(' ', end=blank)
    for col in range(x_min, x_max+1):
        print(f'{col} ', end=blank)


if __name__ == '__main__':
    from vector import Vector
    print_matrix([
        Vector(1,2,'J'),
        Vector(2,3,'A'),
        Vector(3,4,'K'),
        Vector(4,5,'E'),
    ])