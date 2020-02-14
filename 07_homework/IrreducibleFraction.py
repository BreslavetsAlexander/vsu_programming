from Fraction import Fraction


class IrreducibleFraction(Fraction):
    def __init__(self, numerator=None, denominator=None):
        super().__init__(numerator, denominator)
        self.reduce()
