import datetime

t = datetime.time(4, 34, 3,900)
print(t)

print(datetime.time.min)
print(datetime.date.min)
print(datetime.time.max)
print(datetime.date.max)
print(datetime.time.resolution)

#datetime
dt = datetime.datetime.now()
print(dt)

# date
d = datetime.date.today()
print(d)
print(d.timetuple())

print(d.day)
print(d.month)
print(d.year)

# replace date
d1 = datetime.date(2015, 3, 15)
print(d1)
d2 = d1.replace(year=1990)
print(d2)

