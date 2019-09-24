user_str = input('str: ')
k = int(input('k: '))
numbers = []

for i in user_str:
    if i >= '0' and i <= '9':
        numbers.append(i)

print(numbers[k - 1])
