def last_digit(a, b):
    if not b:
        return 1
    base_end = a % 10
    if base_end in [0, 1]:
        return base_end
    powers = {
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1],
    }
    possible_last_digits = powers[base_end]
    last_digit_index = b % len(possible_last_digits)
    return possible_last_digits[last_digit_index - 1]


print(last_digit(23, 56))
print(last_digit(231, 41))
print(last_digit(1, 0))
print(last_digit(100 ** 2000, 10 ** 56))
