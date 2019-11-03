values_storage = [[] for x in range(15)]
keys_storage = [[] for x in range(15)]


def hash(key):
    index = sum(list(map(ord, key)))
    index = sum(list(map(int, str(index))))
    return index % len(values_storage)


def set_value(key, value):
    index = hash(key)
    values_storage[index].append(value)
    keys_storage[index].append(key)


def get_element(key):
    index = hash(key)
    j = ''
    for i in range(len(keys_storage[index])):
        if len(keys_storage[index]):
            if keys_storage[index][i] == key:
                j = i
    return values_storage[index][j]


def reset_value(key):
    index = hash(key)
    j = ''
    for i in range(len(keys_storage[index])):
        if len(keys_storage[index]):
            if keys_storage[index][i] == key:
                j = i
                values_storage[index][j] = 0
                keys_storage[index][j] = ''


print(values_storage)
print(keys_storage)

set_value('abc', 1)
set_value('abc', 5)
set_value('bac', 55)
set_value('bac', 75)
set_value('aba', 54)
set_value('aba', 84)
set_value('abad', 814)

print(values_storage)
print(keys_storage)

print(get_element('abc'))
print(get_element('bac'))
print(get_element('aba'))
print(get_element('abad'))

print(values_storage)
print(keys_storage)

reset_value('abc')
reset_value('bac')

print(values_storage)
print(keys_storage)
