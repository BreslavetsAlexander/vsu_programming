lst = []
s = input('s: ')

while s:
    lst.append(s)
    s = input('s: ')

lst = ''.join(sorted(lst, reverse=True))
print(int(lst))
