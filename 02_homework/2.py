from tools import help_fun

lst = ''.join(sorted(help_fun(), reverse=True))
print(int(lst))
