def calculate_brackets(s):
    opened_brackets = list(filter(lambda sym: sym == '(', s))
    closed_brackets = list(filter(lambda sym: sym == ')', s))
    brackets_difference = len(opened_brackets) - len(closed_brackets)
    if len(opened_brackets) > len(closed_brackets):
        return 'missing ' + str(brackets_difference) + ' )'
    elif len(opened_brackets) < len(closed_brackets):
        return 'missing ' + str(abs(brackets_difference)) + ' ('
    return 'Ok'


user_str = input('str: ')
result = calculate_brackets(user_str)
print(result)
