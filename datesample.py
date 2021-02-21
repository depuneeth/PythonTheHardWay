year = 2015

for yr in range(1,3):
    yr = year
    yr = str(year)
    year += 1
    for month in range(1, 13):
        mon = str(month)
        if len(mon) == 1:
            mon = '0' + mon
        days = 32
        if mon == '02':
            days = days - 3
        if mon == '04':
            days = days - 1
        if mon == '06':
            days = days - 1
        if mon == '09':
            days = days - 1
        if mon == '11':
            days = days - 1
        for day in range(1, days):
            x = str(day)
            if len(x) == 1:
                x = '0' + x

            print(f'{yr}-{mon}-{x}')








