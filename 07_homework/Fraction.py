class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def input_fraction(self):
        self.fraction = input('Type a fraction: ')
        self.numerator, self.denominator = self.fraction.split('/')
        self.numerator, self.denominator = int(self.numerator), int(self.denominator)

    def reduce(self):
        a = abs(self.numerator)
        b = abs(self.denominator)
        while a and b:
            if a > b:
                a %= b
            else:
                b %= a
        nod = a + b
        self.numerator //= nod
        self.denominator //= nod
        if self.numerator < 0 and self.denominator < 0:
            self.numerator, self.denominator = abs(self.numerator), abs(self.denominator)
        elif self.denominator < 0:
            self.numerator, self.denominator = 0 - self.numerator, abs(self.denominator)

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
