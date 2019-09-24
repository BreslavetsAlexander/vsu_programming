lst = []
num = ''
s = input('s: ')

while s:
    lst.append(s)
    s = input('s: ')

lst = sorted(lst)[::-1]
for i in lst:
    num += i

print(int(num))
