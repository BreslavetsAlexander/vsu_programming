s = input('s: ')
symbols = {'+', '-', '*', '/', '//', '**'}
operation = ''.join(symbols & set(s))
operation_index = s.find(operation)
x, y = s[:operation_index], s[operation_index + 1:]

if y.find(operation) != -1:
    operation += operation
    y = s[operation_index + 2:]

x, y = float(x), float(y)
operations = {
    '+': x + y,
    '-': x - y,
    '*': x * y,
    '/': x / y,
    '//': x // y,
    '**': x**y
}
print(operations[operation])
