from typing import List
import math
import timeit

def factorial(n: int) -> int:
    """Given a positive integer n, return n!"""
    # Pre:
    assert n > 0
    result: int = 1
    for i in range(1, n+1):
        result = result * i
    return result

def main(args:List[str]) -> int:
    n: int = int(input('Please enter a positive integer: '))
    assert n > 0, 'n must be positive'
    for i in range(3):
        cmd: str = 'math.factorial({0})'.format(n)
        time: float = timeit.timeit(stmt=cmd, globals=globals())
        print('n =', n, 't(n) =', time)
        n = 10 * n

    # Conventional return value indicating successful completion
    return 0

# factorial(n):    
# n = 2 t(n) = 0.30840749997878447
# n = 20 t(n) = 1.0579672000021674
# n = 200 t(n) = 14.95398180000484

# math.factorial(n):
# n = 3 t(n) = 0.06210999999893829
# n = 30 t(n) = 0.3241042000008747
# n = 300 t(n) = 5.095239099988248

if __name__ == '__main__':
    import sys
    main(sys.argv)