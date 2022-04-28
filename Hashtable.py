from typing import List, Optional, Tuple

def letterhash(key: str) -> int:
    """Simple-minded hash function for letters."""
    result = 0
    key = key.lower() # Ignore case
    for c in key:
        if c.isalpha(): # Only deal with letters
            result = result * 26
            result = result + (ord(c) - ord('a') + 1)
    return result

class Hashtable(object):
    """Class to represent a hash table for (string, string) pairs.
      Uses hash chaining to handle hash collisions."""

    def __init__(self, initial_capy: int = 3):
        """Create an empty Hashtable with initial capacity
        INITIAL_CAPY (default 3)."""
        # hash table
        self._table: List[List[Tuple[str, str]]] = []
        for i in range(initial_capy):
            self._table.append([])
        #print(initial_capy, len(self._table))
        # Size of the table (not number of elements!)
        self._size: int = initial_capy
        # Keys present in the table
        self._keys: List[str] = []

    def _hash(self, key: str) -> int:
        """Hash a key value for this table."""
        return letterhash(key) % self._size

    def put(self, key: str, value:str) -> None:
        """Put a (key, value) pair into the hashtable."""
        if key not in self._keys:
            self._keys.append(key)
            self._table[self._hash(key)].append( (key, value) )
        else:
            raise ValueError('Key "' + key + '" already in table.')

    def get(self, key: str) -> Optional[str]:
        """Return the value associated with KEY, or None
           if KEY is not in the table."""
        result: Optional[str] = None
        if key in self._keys:
            hashval: int = self._hash(key)
            for item in self._table[hashval]:
                if key == item[0]:
                    result = item[1]
        return result





def main(args:List[str]) -> int:
    # Do nothing, successfully

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)