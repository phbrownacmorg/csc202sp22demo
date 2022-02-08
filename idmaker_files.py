from typing import List

def readNames(infilename:str) -> List[List[str]]:
    # Pre: infilename exists AND
    #      infilename is a readable CSV file with a header line AND
    #      each line in infilename has the format:
    #         <something>,last name,first name,middle name,<maybe more>
    nameList:List[List[str]] = []
    with open(infilename,'r') as infile:
        linelist: List[str] = infile.readlines()
        for line in linelist[1:]: # All but first line
            # This is the other place to put the loop invariant
            parts:List[str] = line.split(',')
            last:str = parts[1].strip()
            first:str = parts[2].strip()
            middle:str = parts[3].strip()
            nameList.append([last, first, middle])
            # Loop invariant:
            assert len(parts) > 3 and \
                len(nameList) <= (len(linelist) - 1) and \
                len(nameList[-1]) == 3 and len(last) > 0
                # AND nameList is one longer than it was last time
            assert len(last) > 0

    # Post: namelist has one fewer entries than infilename has lines AND
    #       each entry in namelist is [last, first, middle] AND
    #       each entry in nameList has len(last) > 0
    return nameList

def makeOneUserid(parts:List[str]) -> str:
    # Make and return a single userid, given a List containing
    # the names of the person.
    # Pre:
    assert len(parts) == 3 and len(parts[0]) > 0
    # AND parts is [last name, first name, middle name]

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

    # Post: return value is a Converse-style userid ending in '001'
    return (first[:1] + middle[:1] + last + '001')

def makeUserids(nameList:List[List[str]]) -> List[List[str]]:
    # Given a list of names, make and return a list of userids.  The userid entry 
    # for each person has the form [userid, last name, first name, middle name].
    # Pre: for every entry n on nameList, len(n) == 3 and len(n[0]) > 0
    idList:List[List[str]] = []
    for name in nameList: # type: List[str]
        idList.append([makeOneUserid(name)] + name.copy())
        # Loop invariant:
        assert (len(idList[-1]) == 4) and idList[-1][1:] == name
        # AND idList[-1] is [userid, last name, first name, middle name]

    # Post: every entry on idList is [userid, last, first, middle] AND
    assert len(idList) == len(nameList)
    return idList

def write_userids(idList:List[List[str]], outfilename:str) -> None:
    # Pre: all the entries on idList have the same length AND
    #      outfilename is writable
    with open(outfilename,'w') as outfile:
        for entry in idList: # type: List[str]
            for part in entry[:-1]: # type: str
                outfile.write(part + ',')
            outfile.write(entry[-1] + '\n')
    # Post: all the entries in idList have been written to outfile

def main(args:List[str]) -> int:
    names:List[List[str]] = readNames('namegenerator.csv')
    idList:List[List[str]] = makeUserids(names)
    write_userids(idList, 'userids.csv')
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)