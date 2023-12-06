import functools


def test(expected_output, filename=None, parser=None, data=None):
    """Wraps a function by first calling it on a test input file OR data, and verifying its expected output"""
    def test_wrapper(f):
        functools.wraps(f)

        def run_test(*args, **kwargs):
            out = f(data, **kwargs) if data is not None else f(parser(filename), **kwargs)
            if out != expected_output:
                raise Exception(f"Output {out} != expected {expected_output}")
            return f(*args, **kwargs)

        return run_test

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
