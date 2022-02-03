from typing import List, Tuple
import math

def roots(a:float, b:float, c:float) -> Tuple[float, float]:
    determinant:float = b**2 - 4*a*c
    root1 = (-b + math.sqrt(determinant)) / 2*a
    root2 = (-b - math.sqrt(determinant)) / 2*a
    return root1, root2

def main(args:List[str]) -> int:
    # Do nothing, successfully
    # Read the coefficients
    print('Please enter coefficients for the\nquadratic a*x**2 + b*x + c = 0')
    try:
        a:float = float(input('\ta: '))
        b:float = float(input('\tb: '))
        c:float = float(input('\tc: '))
    except ValueError: # input problem
        print('a, b, and c must be floating-point numbers.')
    else:
        print('The system ' + str(a) + '*X**2 + ',end='')
        print(str(b) + '*X +',c,'= 0')
        print('has the following roots:')

        try:
            root1, root2 = roots(a, b, c) # type: (float, float)
        except ValueError: # Negative determinant
            print('\tNo real roots')
        else:
            print('\t', root1, 'and', root2)

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)