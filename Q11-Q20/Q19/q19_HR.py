# score - 28.57


def run(date_start=1, month_start=1, year_start=1901, date_end=1, month_end=1, year_end=2000):
    no_of_days = sunday = 0
    for yr in range(year_start, year_end + 1):
        ys = ye = False
        if yr == year_start:
            ys = True
            months = range(month_start, 13)
        elif yr == year_end:
            ye = True
            months = range(1, month_end + 1)
        else:
            months = range(1, 13)
        for month in months:
            if ye and month == month_end:
                dmax = date_end
            else:
                if month in [4, 6, 9, 11]:
                    dmax = 30
                elif month == 2:
                    dmax = 29 if yr % 400 == 0 or (yr % 4 == 0 and yr % 100 != 0) else 28
                else:
                    dmax = 31

            if ys and month == month_start:
                days = range(date_start, dmax + 1)
            else:
                days = range(1, dmax + 1)

            # for x in days:
            #     print(no_of_days, x, month, yr, day_name[(no_of_days + x) % 7], (no_of_days + x) % 7)
            #     if x == 1 and (no_of_days + x) % 7 == 0:
            #         print(x, month, yr)

            if year_start <= yr <= year_end:
                if (no_of_days + 1) % 7 == 0:
                    # print(1, month, yr)
                    sunday += 1

            no_of_days += len(days)

    print(sunday)
    return


t = int(input().strip())
for counter in range(t):
    yrs, ms, ds = input().strip().split(' ')
    yre, me, de = input().strip().split(' ')
    yrs, ms, ds = [int(yrs), int(ms), int(ds)]
    yre, me, de = [int(yre), int(me), int(de)]
    run(ds, ms, yrs, de, me, yre)
