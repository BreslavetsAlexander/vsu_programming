user_str = input('str: ').split()

s = list(map(lambda x: len(x), user_str))
print(user_str[s.index(max(s))])

words_collection = set(user_str)
s = []
for i in words_collection:
    s.append(user_str.count(i))

print(list(words_collection)[s.index(max(s))])
