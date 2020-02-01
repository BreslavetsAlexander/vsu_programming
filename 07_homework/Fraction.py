class Fraction:
    def __init__(self):
        self.numerator = self.denominator = None

    def input_fraction(self):
        self.fraction = input('Type a fraction: ')
        self.numerator, self.denominator = self.fraction.split('/')
        self.numerator, self.denominator = int(self.numerator), int(self.denominator)

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
