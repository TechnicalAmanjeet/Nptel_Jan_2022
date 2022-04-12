import pytz
from datetime import datetime as dt

timezone = pytz.all_timezones
print(timezone[0])
# print(timezone[0])

for i in range(len(timezone)):
    print(f"{timezone[i]} : {dt.now(pytz.timezone(timezone[i]))}")
