emp_id = 101
emp_name = 'Yahia Momtaz'
emp_gross_salary = 7000.23

if emp_gross_salary >= 5000:
    tax = 10
else:
    tax = 0

emp_monthly_net_salary = emp_gross_salary - (emp_gross_salary * tax / 100)
annual_net_salary = emp_monthly_net_salary * 12

print(tax)
print('Monthly net salary = '+str(emp_monthly_net_salary))
print('Annual net salary '+str(annual_net_salary))