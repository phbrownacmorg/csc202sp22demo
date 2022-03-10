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