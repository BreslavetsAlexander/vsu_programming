def print_feb_nums(n):
    feb_list = [0, 1]
    for i in range(n - 2):
        feb_list.append(feb_list[-1] + feb_list[-2])
    print(feb_list)


num = int(input('num: '))
print_feb_nums(num)
