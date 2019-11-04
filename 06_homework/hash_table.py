storage = [[] for x in range(15)]


def hash(key):
    index = sum(list(map(ord, key)))
    index = sum(list(map(int, str(index))))
    return index % len(storage)


def set_value(key, value):
    index = hash(key)
    for i in storage[index]:
        if key == i[0]:
            i[1] = value
            break
    else:
        storage[index].append([key, value])


def get_value(key):
    index = hash(key)
    for i in storage[index]:
        if key == i[0]:
            return i[1]


def reset_value(key):
    index = hash(key)
    for i in storage[index]:
        if key == i[0]:
            i[1] = 0
            break


print(storage)

set_value('abc', 10)
set_value('abc', 100)

set_value('bac', 20)
set_value('bac', 120)

set_value('b', 10)
set_value('b', 20)

print(get_value('abc'))
print(get_value('bac'))
print(get_value('b'))

print(storage)

reset_value('abc')

print(storage)
