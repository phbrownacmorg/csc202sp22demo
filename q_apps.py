from Stack import Stack
from CircQ import Queue

def is_palindrome(instring: str) -> bool:
    valid: bool = True

    s: Stack = Stack[str]()
    q: Queue = Queue[str]()

    instring = instring.lower()
    for c in instring: # type: str
        if c.isalpha(): # Only letters
            s.push(c)
            q.add(c)

    while (not s.empty()) and (not q.empty()):
        if s.pop() != q.pop():
            valid = False 

    return valid