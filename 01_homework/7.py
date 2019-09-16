x = int(input('x: '))
y = int(input('y: '))
sum = 0

for num in range(x, y+1):
    if num%5 == 0:
        sum += num

print(sum)