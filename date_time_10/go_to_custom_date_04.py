# program to go to a specific day in a date
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now() # 13-7-2024
print(today)

print('--- Go to the first day in this month ---') # 1-7-2024
first_date = today + relativedelta(day=1)   # 1-7-2024
print('first day = ', first_date)

print('--- Go to the last day in this month ---') # 31-7-2024
last_date = today + relativedelta(day=31) # 31-7-2024
print('Last day = ', last_date)
# problem :

print('-- Go to the last day in the next month---') # 31-8-2024
next_month_last_date = today + relativedelta(months=1, day=31)

print('Next month last day = ', next_month_last_date)

print('--- The Nearest Sunday from today -----')
nearest_sunday = today + relativedelta(weekday=calendar.SUNDAY)
print('Nearest sunday = ', nearest_sunday)



print('--- The Nearest 2nd sunday from today -----')
nearest_2nd_sunday = today + relativedelta(weekday=calendar.SUNDAY, weeks=1)
print('The Nearest 2nd sunday from today = ', nearest_2nd_sunday)





