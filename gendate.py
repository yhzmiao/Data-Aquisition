import datetime
begin = datetime.date(2019,12,1)
end = datetime.date(2020,3,1)
day = begin
delta = datetime.timedelta(days=1)

f = open("date.txt", 'w')

while day <= end:
	print >> f, day.strftime("%Y-%m-%d")
	day += delta
