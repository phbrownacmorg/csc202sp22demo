from typing import cast, List, Tuple

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
    if (a % b) == 0: # Base case: b divides a evenly
        result = b
    else: # Recursive case
        result = gcd(b, a % b)
    return abs(result) # abs to handle negatives correctly

def main(args: List[str]) -> int:
    numlist = list(range(3))
    print(numlist, sumlist(cast(List[float], numlist)))
    s = 'The quick brown fox'
    print(s, ':', strrev(s))
    a, b = 5, 11 # type: Tuple[int, int]
    print('gcd(', a, ',', b, ') = ', gcd(a, b), sep='')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))