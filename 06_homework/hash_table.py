codes_storage = [0 for x in range(15)]
strings_storage = ['' for x in range(15)]


def hash(key):
    return len(key) % len(codes_storage)


def rehash(old_hash):
    return (old_hash + 1) % len(codes_storage)


def set_value(key, value):
    index = hash(key)
    while codes_storage[index]:
        index = rehash(index)
    codes_storage[index] = value
    strings_storage[index] = key


def get_element(key):
    return codes_storage[strings_storage.index(key)]


def reset_value(key):
    codes_storage[strings_storage.index(key)] = 0
    strings_storage[strings_storage.index(key)] = ''


print(codes_storage)
print(strings_storage)

set_value('abc', 1)
set_value('bca', 6)
set_value('ba', 7)
set_value('bc', 71)

print(get_element('abc'))
print(get_element('bca'))
print(get_element('ba'))
print(get_element('bc'))

print(codes_storage)
print(strings_storage)

reset_value('ba')
reset_value('bc')

print(codes_storage)
print(strings_storage)
