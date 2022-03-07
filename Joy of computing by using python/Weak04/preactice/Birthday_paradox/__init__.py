import random
import datetime


def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False

# print(leap_year(40))


# ****** main program ***********
birth_day = []
birth_year = []
month_31 = [1, 3, 5, 7, 8, 10, 12]
i = 0

while i < 100:
    leap = 0
    year = random.randint(1985, 2021)
    if leap_year(year):
        leap = 1

    month = random.randint(1, 12)
    if month == 2:
        day = random.randint(1, leap + 28)
    elif month in month_31:
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)

    dd = datetime.date(year, month, day)
    day_of_year = dd.timetuple().tm_yday
    birth_day.append(day_of_year)
    # print(day_of_year)
    i += 1

birth_day.sort()
print(birth_day)
