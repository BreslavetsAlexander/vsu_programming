values_storage = [[] for x in range(15)]
keys_storage = [[] for x in range(15)]


def hash(key):
    index = sum(list(map(ord, key)))
    index = sum(list(map(int, str(index))))
    return index % len(values_storage)


def set_value(key, value):
    index = hash(key)
    if keys_storage[index].count(key) < 1:
        keys_storage[index].append(key)
        values_storage[index].append(value)
    values_storage[index][-1] = value


def get_element(key):
    index = hash(key)
    return values_storage[index][-1]


def reset_value(key):
    index = hash(key)
    j = ''
    for i in range(len(keys_storage[index])):
        if len(keys_storage[index]):
            if keys_storage[index][i] == key:
                j = i
                values_storage[index][j] = 0
                keys_storage[index][j] = ''


set_value('abc', 1)
set_value('abc', 2)
set_value('abc', 22)
set_value('abd', 225)
set_value('abd', 220)

print(get_element('abc'))
print(get_element('abd'))

print(values_storage)
print(keys_storage)

reset_value('abc')

print(values_storage)
print(keys_storage)
