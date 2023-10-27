import datetime

t = datetime.time(4, 34, 3,900)
print('time->',t)

t2 = datetime.datetime(1994,7,21,4,34,3,900)
print('date time->',t2)

print(datetime.time.min)
print(datetime.date.min)
print(datetime.time.max)
print(datetime.date.max)
print(datetime.time.resolution)

#datetime now
dt = datetime.datetime.now()
print(f'data time now -->',dt)

# date
d = datetime.date.today()
print('datetime today -->',d)
print(d.timetuple())

print('day',d.day)
print('month',d.month)
print('week day',d.weekday())
print('year',d.year)

# replace date
print('replace date')
d1 = datetime.date(2015, 3, 15)
print(d1)
d2 = d1.replace(year=1990)
print(d2)

