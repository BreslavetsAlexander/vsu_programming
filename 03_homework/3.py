def print_feb_nums(n):
    feb_list = [0, 1]
    for i in range(n - 2):
        last = feb_list[-1]
        penultimate = feb_list[-2]
        feb_list.append(last + penultimate)
    print(feb_list)


num = int(input('num: '))
print_feb_nums(num)
