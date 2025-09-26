emp_code = 101
emp_name = 'Usama Omar'
emp_salary = 7000.56
emp_job = 'Web Developer'
emp_city = 'Cairo'

# Usama Omar works as Web Developer and lives in Cairo
print(emp_name + 'works as '+emp_job + ' and lives in '+ emp_city)

print('-------------- Casting --- Convert from data type to another -------from int, float to string ----')
# ex :  Usama Omar takes salary = 7000.55
print(emp_name + ' takes salary = '+ str(emp_salary))
print(emp_name, 'takes salary =', emp_salary)
print(f'{emp_name} take salary = {emp_salary}')


# ex: Usama Omar has code = 101
print(emp_name + ' has code = '+ str(emp_code))





print('---- casting ----- convert from float to int --------------------')
print(emp_salary)
print(int(emp_salary))
print(round(emp_salary, 1))

