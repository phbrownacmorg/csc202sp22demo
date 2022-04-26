from typing import Iterable, List, Protocol, Sequence, TypeVar

T = TypeVar('T')

def seqsearch(items:Iterable[T], key:T) -> int:
    """Perform a sequential search for KEY in ITEMS.
    Returns the index of KEY in ITEMS, or raises
    ValueError if KEY is not present.  This mimics
    the behavior of the index() method for a sequence."""
    result: int = -1
    idx: int = -1

    # Iterate over the items, looking...
    for item in items:
        idx = idx + 1
        if (key == item):
            result = idx
            break
    if result < 0: # Didn't find it
        raise ValueError('Item not found')
    return result

def binsearch(items:Sequence[T], key:T) -> int:
    """Perform a binary search for KEY in ITEMS.
    Returns the index of KEY in ITEMS, or raises
    ValueError if KEY is not present.  This mimics
    the behavior of the index() method for a sequence."""
    # Precondition: items is sorted in ascending order
    
    if len(items) == 0: # Base case #1: the item isn't here
        raise ValueError('Item not found.')
    else:
        mid: int = len(items) // 2
        result: int = -1
        if key == items[mid]: # Base case #2
            result = mid
        # Recursive case #1
        elif key < items[mid]: # type: ignore
            result = binsearch(items[:mid], key)
        else: # key > items[mid], recursive case #2
            result = (mid+1) + binsearch(items[mid+1:], key)
        return result


def main(args:List[str]) -> int:
    # Do nothing, successfully

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)
