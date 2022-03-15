from Stack import Stack

# ------- Delimiter matching -----------------

def match_delimiters(instring:str) -> bool:
    """Function to tell whether a string has
    balanced delimiters (parentheses, braces,
    and angle brackets).  Only single-character
    delimiters are supported."""
    left_delims: str = '({[<'
    right_delims: str = ')}]>'

    matched: bool = True
    stack: Stack[str] = Stack[str]()

    for c in instring:
        if c in left_delims:
            stack.push(c)
        elif c in right_delims:
            if stack.empty():
                matched = False
            elif right_delims.index(c) != left_delims.index(stack.pop()):
                matched = False
    if not stack.empty():
        matched = False
    return matched
    

# -- Converting a number from one base to another --

def convert_bases(num: int, base: int) -> str:
    """Convert the number NUM to the base BASE, and return the
    resulting string."""
    digits: str = "0123456789abcdefghijklmnopqrstuvwxyz"
    # Pre:
    assert 2 <= base <= len(digits)

    s: Stack = Stack[str]()

    result: str = ''
    if num < 0:
        result = '-'
        num = -num
    
    while num > 0:
        digit = num % base
        s.push(digits[digit])
        num = num // base

    if s.empty():
        result = result + '0'
    else:
        while not s.empty():
            result = result + s.pop()
    
    return result

