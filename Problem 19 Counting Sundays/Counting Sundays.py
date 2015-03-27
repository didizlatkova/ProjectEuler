# You are given the following information, but you may prefer to do some research for yourself.
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def dayOfWeek(day, month, year):
    a = (14 - month) / 12
    y = year - a
    m = month + 12*a - 2

    return (day + y + y/4 - y/100 + y/400 + (31*m)/12) % 7

count = 0

for year in range(1901,2001):
    for month in range(1,13):
        if (dayOfWeek(1, month, year) == 0):
            count += 1

print(count)