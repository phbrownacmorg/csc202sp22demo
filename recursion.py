from typing import cast, List, Tuple
import random
import turtle

# ----------------- Sum a list of numbers ---------------------------

def sumlist_iterative(numlist: List[float]) -> float:
    """Sum a list of numbers, iteratively."""
    result: float = 0
    for num in numlist:
        result = result + num
    return result

def sumlist_recursive(numlist: List[float]) -> float:
    """Sum a list of numbers, recursively."""
    result: float = 0
    if len(numlist) == 0: # Base case, empty list
        result = 0
    else: # Recursive case
        # Sum is the first element plus the sum of the rest of the list
        result = numlist[0] + sumlist_recursive(numlist[1:])
    return result

def sumlist(numlist: List[float]) -> float:
    return sumlist_recursive(numlist)

# ----------- String reversal --------------------------

def strrev(s: str) -> str:
    """Reverse a string, recursively."""
    result: str = ''
    if len(s) <= 1: # Base case: strrev(s) == s
        result = s
    else: # Recursive case
        # Move one character to the other end and reverse what's left
        result = s[-1] + strrev(s[:-1])
    return result

# -------------- GCD ----------------------------------

def gcd(a: int, b: int) -> int:
    """Find the GCD, recursively."""
    result: int = 0
    if b == 0:
        result = a
    elif (a % b) == 0: # Base case: b divides a evenly
        result = b
    else: # Recursive case
        result = gcd(b, a % b)
    return abs(result) # abs to handle negatives correctly

# -------------- Exponentiation -----------------------

def exp(a: float, b: int) -> float:
    """Raise a**b recursively."""
    result: float = 0

    if b == 0:
        result = 1
    elif b < 0:
        result = 1 / exp(a, -b)
    else: # b > 0
        result = a * exp(a, b - 1)
    return result

# -------------- Fast exponentiation -----------------------
# (also allows the use of much larger powers without running
# afoul of the maximum recursion depth)

def fastexp(a: float, b: int) -> float:
    """Raise a**b recursively, but faster."""
    result: float = 0

    if b == 0: # Base case
        result = 1
    elif b < 0:
        result = 1 / fastexp(a, -b)
    elif (b % 2) == 0: # Recursive case #1: b > 0 and b is even
        root: float = fastexp(a, b // 2)
        result = root * root # Square the square root
    else: # Recursive case #2: b > 0 and b is odd
        root = fastexp(a, b // 2)
        result = a * root * root # Square the square root
    return result

#-------------- Base conversion ---------------------------------

def baseconv(a: int, b: int) -> str:
    """Return a expressed in base b."""
    digits: str = '0123456789abcdefghijklmnopqrstuvwxyz'
    # Pre:
    assert b > 1 and b <= len(digits)

    result: str = ''

    if a >= 0 and a < b: # Base case
        result = digits[a]
    elif a < 0: # Recursive case #1
        result = '-' + baseconv(-a, b)
    else: # Recursive case #2
        result = baseconv(a // b, b) + digits[a % b]
    return result

# ------- Fibonacci --------------------

def slowfib(n: int) -> int:
    """Calculate the n'th Fibonacci number, recursively.
    This is coded straight from the definition, which results
    in something correct but unusably slow."""
    # Pre:
    assert n >= 0

    result: int = n # Handles the two base cases
    if n > 1: # Recursive case
        result = slowfib(n-1) + slowfib(n-2)
    return result

def fastfib(n: int) -> Tuple[int, int]:
    """Recursive Fibonacci, remembering previous results.
    This version returns not a single number but a tuple of
    (fib(n), fib(n-1)).  This gives a result in O(n) time."""
    # Pre:
    assert n >= 0
    result: Tuple[int, int] = (n, 0) # Base cases
    if n > 1: # Recursive case
        n_less_1: Tuple[int, int] = fastfib(n-1)
        result = (n_less_1[0] + n_less_1[1], n_less_1[0])
    return result

def fib(n: int) -> int:
    """Calculate the n'th Fibonacci number."""
    return fastfib(n)[0]

# ------------- Towers of Hanoi ----------------------------

def move_tower(height: int, from_pole: str, to_pole: str, 
            with_pole: str) -> None:
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(height, from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)

def move_disk(disk: int, from_p: str, to_p: str) -> None:
    print("moving disk", disk, "from", from_p, "to", to_p)

#move_tower(4, "A", "B", "C")

# Graphical recursions
def tree(branch_len: int, t: turtle.Turtle) -> None:
    if branch_len > 5:
        t.width(branch_len // 5)
        if branch_len < 40:
            t.color('green')
        else:
            t.color('brown')
        t.down()
        t.forward(branch_len)
        angle: float = 15 + 10 * random.random()
        t.right(angle)
        tree(branch_len - 15, t)
        t.left(2 * angle)
        tree(branch_len - 15, t)
        t.right(angle)
        t.up()
        t.backward(branch_len)

def draw_tree() -> None:
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    my_win.exitonclick()


def main(args: List[str]) -> int:
    numlist = list(range(3))
    print(numlist, sumlist(cast(List[float], numlist)))
    s = 'The quick brown fox'
    print(s, ':', strrev(s))
    a, b = 5, 11 # type: Tuple[int, int]
    print('gcd(', a, ',', b, ') = ', gcd(a, b), sep='')
    a, b = 2, 900  # 996
    print(a, "**" , b, '=', exp(a, b))
    print(a, "**" , b, '=', fastexp(a, b))
    b = 1000000
    # print(a, "**" , b, '=', fastexp(a, b))
    a, b = 256, 10
    print(a, 'in base', b, '=', baseconv(a, b))
    a, b = 256, 16
    print(a, 'in base', b, '=', baseconv(a, b))
    a, b = 256, 2
    print(a, 'in base', b, '=', baseconv(a, b))
    a, b = 255, 10
    print(a, 'in base', b, '=', baseconv(a, b))
    a, b = 255, 16
    print(a, 'in base', b, '=', baseconv(a, b))
    a, b = 255, 2
    print(a, 'in base', b, '=', baseconv(a, b))


    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))