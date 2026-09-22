#date_time

from datetime import datetime
now=datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

#present date
from datetime import date
print(date.today())
#manual setting of date
d=date(2016,7,10)
print(d)

#future & past date
from datetime import timedelta
today=date.today()
future=today+timedelta(days=20)
print(future)
past=today-timedelta(days=3)
print(past)

#foramting dates
from datetime import datetime
now=datetime.now()
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%d/%m/%y"))
print(now.strftime("%H:%M:%S"))
