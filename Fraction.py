import math
from typing import Any

class Fraction:
    """Class to represent a rational number.  Fraction objects are
    immutable."""

    def _invariant(self) -> bool:
        """Class invariant for Fraction.  Each Fraction is stored
        in lowest terms.  Improper fractions are allowed."""
        return (self.denom > 0) and math.gcd(self.num, self.denom) == 1

    def __init__(self, num: int, denom: int):
        """Construct a valid Fraction from a given numerator and denominator."""
        # Pre:
        assert denom != 0
        divisor: int = math.gcd(num, denom)
        if denom < 0:
            divisor = -divisor
        self.num: int = num // divisor
        self.denom: int = denom // divisor
        # Post:
        assert self._invariant()

    def __str__(self) -> str:
        """Represent the Fraction as a string."""
        # Pre:
        assert self._invariant()
        result: str = "{0}/{1}".format(self.num, self.denom)
        # Post: result actually represents the Fraction
        return result

    def __eq__(self, other: Any) -> bool:
        """Test whether two Fractions are equal."""
        # Pre:
        assert self._invariant()
        if not isinstance(other, Fraction):
            raise NotImplementedError('Fraction cannot be compared to ' + str(type(other)))
        result: bool = (self.num == other.num and self.denom == other.denom)
        # Post: result is True iff the numerators and denominators are equal AND
        assert isinstance(other, Fraction)
        return result


    # Put the class name in quotation marks when using it
    #  in type annotations, because it's not yet defined.
    def __add__(self, other: 'Fraction') -> 'Fraction':
        """Add two Fractions."""
        # Pre:
        assert self._invariant() and other._invariant()
        result = Fraction(self.num * other.denom + other.num * self.denom,
                          self.denom * other.denom)
        # Post: result == self + other
        # (Executable assertion would just repeat the function)
        return result