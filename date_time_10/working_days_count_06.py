
# program to get the date after 12 working days from a date
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()
jump_working_days = 12

# start date = 13-7-2024        end_date = 29-7-2024

required_date = today

for i in range(jump_working_days):
    if required_date.date().weekday() == 3: # thursday
        required_date = required_date + relativedelta(days=3)
    elif required_date.date().weekday() == 4: # friday [ only once if the start date is friday ]
        required_date = required_date + relativedelta(days=2)
    else:
        required_date = required_date + relativedelta(days=1)

print('The target date = ', required_date)




