from typing import List
import copy

def print3Lists(one: List, two: List, three: List) -> None:
    print("List1:", one)
    print('List2:', two)
    print('List3:', three)
    print()

def checkAlias(one: object, two: object) -> None:
    if one is two:
        print(id(one), 'aliases', id(two))
    else:
        print(id(one), 'DOES NOT alias', id(two))

def main(args: List[str]) -> int:
    quickFox1: List[str] = ['The', 'quick', 'brown', 'fox']
    dogsback1: List[str] = ['the', 'lazy', "dog's", 'back']
    verb1: List[str] = ['jumped', 'over']

    list1: List[List[str]] = [quickFox1, verb1, dogsback1]

    # Shallow copy
    list2: List[List[str]] = copy.copy(list1) # Same as list1[:]

    # Deep copy
    list3: List[List[str]] = copy.deepcopy(list2)

    print3Lists(list1, list2, list3)

    # Swap first and last items in list1
    list1[0], list1[2] = list1[2], list1[0]

    print3Lists(list1, list2, list3)

    #list2[0][1], list2[0][2] = list2[0][2], list2[0][1]
    quickFox1[1], quickFox1[2] = quickFox1[2], quickFox1[1]
    # Danger, Will Robinson!  This change also changes list1[2]
    #   and list2[0].  This is aliasing.

    print3Lists(list1, list2, list3)

    checkAlias(list1, list2)
    checkAlias(list1, list3)
    checkAlias(list1[0], list2[2])
    checkAlias(list1[2], quickFox1)

    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)