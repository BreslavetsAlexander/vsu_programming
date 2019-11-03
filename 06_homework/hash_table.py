storage = [[] for x in range(15)]


def hash(key):
    index = sum(list(map(ord, key)))
    index = sum(list(map(int, str(index))))
    return index % len(storage)


def set_value(key, value):
    index = hash(key)
    if not storage[index]:
        storage[index] = [[key, value]]
    else:
        for i in range(len(storage)):
            for j in range(len(storage[i])):
                if storage[i][j][0] == key:
                    storage[i][j][1] = value
                    break
                else:
                    storage[i].append([key, value])
                    break


def get_value(key):
    index = hash(key)
    for i in range(len(storage[index])):
        if key == storage[index][i][0]:
            return storage[index][i][1]


print(storage)

set_value('abc', 10)
set_value('abc', 100)
set_value('abc', 1040)
set_value('bac', 20)
print(get_value('abc'))
print(get_value('bac'))

print(storage)
