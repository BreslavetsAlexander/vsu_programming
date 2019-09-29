def calculate_brackets(s):
    opened_brackets = s.count('(')
    closed_brackets = s.count(')')
    brackets_difference = abs(opened_brackets - closed_brackets)
    if opened_brackets > closed_brackets:
        return 'missing ' + str(brackets_difference) + ' )'
    elif opened_brackets < closed_brackets:
        return 'missing ' + str(brackets_difference) + ' ('
    return 'Ok'


user_str = input('str: ')
result = calculate_brackets(user_str)
print(result)
