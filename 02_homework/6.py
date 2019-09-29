user_str = input('str: ')
k = int(input('k: '))

user_str = list(filter(lambda s: s.isdigit(), user_str))
print(user_str[k - 1])
