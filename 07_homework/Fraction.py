class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def input_fraction(self):
        self.fraction = input('Type a fraction: ')
        self.numerator, self.denominator = self.fraction.split('/')
        self.numerator, self.denominator = int(self.numerator), int(self.denominator)

    def reduce(self):
        a = self.numerator
        b = self.denominator
        while a and b:
            if a > b:
                a = a % b
            else:
                b = b % a
        nod = a + b
        self.numerator //= nod
        self.denominator //= nod

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
