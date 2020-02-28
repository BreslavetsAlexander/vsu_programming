from Fraction import Fraction


class IrreducibleFraction(Fraction):
    def __init__(self, numerator=0, denominator=1):
        super().__init__(numerator, denominator)
        self.reduce()
