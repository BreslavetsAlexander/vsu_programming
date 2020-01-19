class Fraction:
    def __init__(self):
        self.numerator = self.denominator = None

    def input_fraction(self):
        self.fraction = input('Type a fraction: ')
        slash_index = self.fraction.index('/')
        self.numerator = self.fraction[:slash_index]
        self.denominator = self.fraction[slash_index + 1:]

    def print_fraction(self):
        print(f'{int(self.numerator)}/{int(self.denominator)}')
