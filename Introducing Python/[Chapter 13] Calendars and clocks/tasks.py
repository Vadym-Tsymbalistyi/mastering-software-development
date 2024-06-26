# 13.1 Write the current date as a string to the text file today.txt.
from datetime import datetime

now = datetime.today()
print(now)
now = now.isoformat()
with open('today.txt', 'wt') as output:
    print(now, file=output)

# 13.2 Read the text file today.txt into the string today_string.
with open('today.txt', 'rt') as input:
    today_string = input.read()
print(today_string)

# 13.3 Parse the date from today_string.
date_object = datetime.strptime(today_string, "%Y-%m-%dT%H:%M:%S.%f\n")
print(date_object)

# 13.4 Create a date object of your day of birth.
from datetime import date

birthday = date(2001, 5, 25)
print(birthday)

# 13.5 What day of the week was your day of birth?
birthday.isoweekday()
print(birthday.isoweekday())

# 13.6 When will you be (or when were you) 10,000 days old?
from datetime import timedelta

n_day = birthday + timedelta(days=10000)
print(n_day)
