# -*- coding: utf-8 -*
import datetime
import time
t = datetime.time(18,59,30,10)
print t
print t.hour
print t.minute
print t.second
print t.microsecond
print t.tzinfo

today = datetime.date.today()
print today
print today.ctime()
tt = today.timetuple()
print tt.tm_year
print tt.tm_mon
print tt.tm_hour
print tt.tm_min
print tt.tm_sec
print tt.tm_wday
print tt.tm_yday
print tt.tm_isdst

o=733114
print datetime.date.fromordinal(o)
t = time.time()
print datetime.date.fromtimestamp(t)

print datetime.date.min
print datetime.date.max
print datetime.date.resolution

d1 = datetime.date(2008,3,29)
print d1.ctime()
d2 = d1.replace(year=2009)
print d2.ctime()

print datetime.timedelta(microseconds=1)
print datetime.timedelta(milliseconds=1)
print datetime.timedelta(seconds=1)
print datetime.timedelta(minutes=1)
print datetime.timedelta(hours=1)
print datetime.timedelta(days=1)
print datetime.timedelta(weeks=1)
print datetime.timedelta(weeks=1).total_seconds()
print datetime.time(18,59,30,10) < datetime.time(18,59,30,20)


print 'Now:',datetime.datetime.now()
print 'Today:',datetime.datetime.today()
print 'UTC Now',datetime.datetime.utcnow()
#结合日期时间
t = datetime.time(1,2,3)
d = datetime.date.today()
print datetime.datetime.combine(d,t)


