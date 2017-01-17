import calendar

date = map(int, raw_input().split())
month, day, year = date[0], date[1], date[2]

print calendar.day_name[calendar.weekday(year, month, day)].upper()
