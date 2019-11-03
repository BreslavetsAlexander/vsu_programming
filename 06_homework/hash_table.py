values_storage = [0 for x in range(15)]
keys_storage = ['' for x in range(15)]


def hash(key):
    return len(key) % len(values_storage)


def rehash(old_hash):
    return (old_hash + 1) % len(values_storage)


def set_value(key, value):
    index = hash(key)
    while values_storage[index]:
        index = rehash(index)
    values_storage[index] = value
    keys_storage[index] = key
    new_index = keys_storage.index(key)
    if index != new_index:
        values_storage[new_index] = value
        reset_value(key)


def get_element(key):
    return values_storage[keys_storage.index(key)]


def reset_value(key):
    index = keys_storage.index(key)
    values_storage[index] = 0
    keys_storage[index] = ''


print(values_storage)
print(keys_storage)

set_value('abc', 1)
set_value('abc', 5)
set_value('aba', 2)
set_value('aba', 10)
set_value('ba', 7)
set_value('ba', 17)
set_value('bc', 71)

print(get_element('abc'))
print(get_element('aba'))
print(get_element('ba'))
print(get_element('bc'))

print(values_storage)
print(keys_storage)

reset_value('ba')
reset_value('bc')

print(values_storage)
print(keys_storage)
