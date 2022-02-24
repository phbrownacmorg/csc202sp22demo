from typing import Any, List, Sequence
import timeit

def measure_length(seq: Sequence[Any]) -> int:
    count: int = 0
    for item in seq:
        count = count + 1
    return count

def read_and_measure(fname: str) -> int:
    with open(fname, 'r') as infile:
        contents: str = infile.read()
        length: int = measure_length(contents)
    return length

def main(args:List[str]) -> int:
    fname: str = input('Please enter a filename: ')

    timeit.timeit('import measure_time; measure_time.read_and_measure({0})'.format(fname))

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)