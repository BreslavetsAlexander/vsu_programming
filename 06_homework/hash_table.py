storage = [0 for x in range(15)]


def hash(key):
    index = sum(list(map(ord, key)))
    index = sum(list(map(int, str(index))))
    return index % len(storage)


def get_element(key):
    index = hash(key)
    return storage[index]


def set_value(key, value):
    index = hash(key)
    storage[index] = value


def reset_value(key):
    index = hash(key)
    storage[index] = 0


print(storage)

set_value('abc', 171)
set_value('xyz', 1)
set_value('bxac', 14)
set_value('Cvposdf[]Fd', 57)
set_value('-a-Df-X', 143)

print(get_element('abc'))
print(get_element('xyz'))
print(get_element('bxac'))
print(get_element('Cvposdf[]Fd'))
print(get_element('-a-Df-X'))

print(storage)

reset_value('bxac')
reset_value('-a-Df-X')

print(storage)
