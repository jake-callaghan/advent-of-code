import functools


def test(input, output):
    """Wraps a function by first calling it on a test input and verifying its expected output"""

    def test_wrapper(f):
        functools.wraps(f)

        def test(*args, **kwargs):
            assert f(input) == output
            return f(*args, **kwargs)

        return test

    return test_wrapper


def write_output(filename):
    """Write a functions output to the specified file"""

    def output_wrapper(f):
        functools.wraps(f)

        def out(*args, **kwargs):
            x = f(*args, **kwargs)
            with open(filename, 'w+') as file:
                file.write(str(x))
            return x

        return out

    return output_wrapper


def print_output(f):
    """Print a functions output"""
    functools.wraps(f)

    def print_wrapper(*args, **kwargs):
        x = f(*args, **kwargs)
        print(x)
        return x

    return print_wrapper
