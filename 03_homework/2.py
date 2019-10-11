def get_season(n):
    seasons = {
        2 < n < 6: 'Spring',
        5 < n < 9: 'Summer',
        8 < n < 12: 'Autumn',
        n in (12, 1, 2): 'Winter',
    }
    return seasons[True]


month = int(input('month: '))
print(get_season(month))
