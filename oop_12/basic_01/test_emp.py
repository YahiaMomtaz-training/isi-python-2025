from oop_12.basic_01.emp import Emp

# main program
# create object
emp_ahmed =(
    Emp(101, 'Ahmed Omar',
            5000, 'dev'))

monthly_net_salary = emp_ahmed.calc_monthly_net_salary()
annual_net_salary = emp_ahmed.calc_annual_net_salary()
print('For Ahmed ', monthly_net_salary, annual_net_salary)


emp_hossam = Emp(employee_id=102, employee_name='hossam aly', employee_salary=5000)

emp_aly = Emp(employee_id=103, employee_name='aly aly', employee_salary=8000)

emp_sheref = Emp(employee_id=104, employee_name='shereef ahmeed', employee_salary=12000)

print('---- List of Employees ---------')
emps_list = [emp_ahmed, emp_hossam, emp_aly, emp_sheref]
emps_list.append( Emp(employee_id=105, employee_name='Mostafa', employee_salary= 9000) )

print('--- loop over list ---')
total_salary = 0
for emp in emps_list:
    if emp.employee_salary < 6000:
        emp.employee_salary = emp.employee_salary + 1000
    print(emp.employee_id, emp.employee_name, emp.calc_monthly_net_salary())
    total_salary = total_salary + emp.calc_monthly_net_salary()

print('total salary= ', total_salary)








