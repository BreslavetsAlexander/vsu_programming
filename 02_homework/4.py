def calculate_brackets(s):
    brackets_difference = abs(s.count('(') - s.count(')'))
    if s.count('(') > s.count(')'):
        return 'missing ' + str(brackets_difference) + ' )'
    elif s.count('(') < s.count(')'):
        return 'missing ' + str(brackets_difference) + ' ('
    return 'Ok'


user_str = input('str: ')
result = calculate_brackets(user_str)
print(result)
