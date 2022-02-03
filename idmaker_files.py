from typing import List

def readNames(infilename:str) -> List[List[str]]:
    nameList:List[List[str]] = []
    with open(infilename,'r') as infile:
        for line in infile.readlines()[1:]: # All but first line
            parts:List[str] = line.split(',')
            last:str = parts[1].strip()
            first:str = parts[2].strip()
            middle:str = parts[3].strip()
            nameList.append([last, first, middle])
    return nameList

def makeOneUserid(parts:List[str]) -> str:
    # Make and return a single userid, given a List containing the names of the person.
    # The list is assumed to be [last name, first name, middle name].  The first and 
    # middle names may be empty.
    last:str = parts[0].lower()
    first:str = parts[1].lower()
    middle:str = parts[2].lower()

    # Remove unwanted characters in the last name
    last = last.replace(' ', '')
    last = last.replace("'", '')

    # Make the userid from the parts.  Slicing is
    # used on the first and middle names to handle
    # the case where either or both of these may not
    # exist (may just be the empty string).
    return (first[:1] + middle[:1] + last + '001')

def makeUserids(nameList:List[List[str]]) -> List[List[str]]:
    # Given a list of names, make and return a list of userids.  The userid entry 
    # for each person has the form [userid, last name, first name, middle name].
    idList:List[List[str]] = []
    for name in nameList: # type: List[str]
        idList.append([makeOneUserid(name)] + name.copy())
    return idList

def write_userids(idList:List[List[str]], outfilename:str) -> None:
    with open(outfilename,'w') as outfile:
        for entry in idList: # type: List[str]
            for part in entry[:-1]: # type: str
                outfile.write(part + ',')
            outfile.write(entry[-1] + '\n')

def main(args:List[str]) -> int:
    names:List[List[str]] = readNames('namegenerator.csv')
    idList:List[List[str]] = makeUserids(names)
    write_userids(idList, 'userids.csv')
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)