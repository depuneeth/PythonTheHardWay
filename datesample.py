year = 2016

for yr in range(1,6):
    yr = str(year)

    for month in range(1, 13):
        mon = str(month)
        if len(mon) == 1:
            mon = '0' + mon
        days = 32
        if mon == '02':
            if year % 4 == 0:
                days = days - 2
                year += 1
            else:
                days = days - 3
                year += 1
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








