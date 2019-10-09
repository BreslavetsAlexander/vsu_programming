s = input('s: ')
oper = ''.join(list(filter(lambda sym: not sym.isdigit() and sym != '.', s)))
x, y = s.replace(oper, ' ').split()
x = float(x)
y = float(y)
operations = {
    '+': x + y,
    '-': x - y,
    '*': x * y,
    '/': x / y,
    '//': x // y,
    '**': x**y
}

print(operations[oper])
