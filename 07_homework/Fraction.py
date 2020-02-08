class Fraction:
    def __init__(self, numerator=None, denominator=None):
        self.numerator = numerator
        self.denominator = denominator
        if not self.numerator or not self.denominator:
            self.input_fraction()

    def input_fraction(self):
        self.fraction = input('Type a fraction: ')
        self.numerator, self.denominator = self.fraction.split('/')
        self.numerator, self.denominator = int(self.numerator), int(self.denominator)

    def reduce(self):
        numerator_dividers = self.find_dividers(self.numerator)
        denominator_dividers = self.find_dividers(self.denominator)
        common_dividers = list(numerator_dividers & denominator_dividers)
        for i in common_dividers[::-1]:
            if not self.numerator % i and not self.denominator % i:
                self.numerator //= i
                self.denominator //= i

    def find_dividers(self, num):
        dividers = set()
        for i in range(2, num):
            if not num % i:
                dividers.add(i)
        return dividers

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
