def calculate_brackets(s):
    brackets = []
    opened_brackets = 0
    closed_brackets = 0
    msg = 'Ok'
    for i in s:
        if i == '(' or i == ')':
            brackets.append(i)
    for b in brackets:
        if b == '(':
            opened_brackets += 1
    closed_brackets = len(brackets) - opened_brackets
    if opened_brackets > closed_brackets:
        msg = 'missing ' + str(opened_brackets - closed_brackets) + ' )'
    elif closed_brackets > opened_brackets:
        msg = 'missing ' + str(closed_brackets - opened_brackets) + ' ('
    return msg


user_str = input('str: ')
result = calculate_brackets(user_str)
print(result)
