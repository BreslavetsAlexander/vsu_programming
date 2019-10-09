s = input('s: ')
lst = []

while s:
    lst.append(s)
    s = input('s: ')

for i in set(lst):
    print(f'{i} - {lst.count(i)}')
