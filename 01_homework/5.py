x = float(input('x: '))
y = float(input('y: '))

if x > 0 and y > 0:
    print('1 четверть')
elif x < 0 and y > 0:
    print('2 четверть')
elif x < 0 and y < 0:
    print('3 четверть')
elif x > 0 and y < 0:
    print('4 четверть')
elif not x or not y:
    print('точка лежит на оси')
