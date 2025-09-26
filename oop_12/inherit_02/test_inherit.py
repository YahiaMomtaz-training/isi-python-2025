# main program
from oop_12.inherit_02.employee import Employee
from oop_12.inherit_02.manager import Manager

print('----- Employee object ------')
emp_ahmed = Employee(person_id=101, person_name='hossam', person_gross_salary=12000,
                     over_time_hours=100, over_time_rate=20)

print(emp_ahmed.person_name)
print(emp_ahmed.calc_monthly_net_salary())


print('----- Manager object ------')
mgr_khaled = Manager(401, 'Khaled Aly', 15000, 'Project Manager', 10)
print('Monthly net salary = ', mgr_khaled.calc_monthly_net_salary())  # 13500
print('Annual net salary = ', mgr_khaled.calc_annual_net_salary())  # 162000
company_profit = 1_000_000.00
print('Annual net salary with profit = ', mgr_khaled.calc_annual_net_salary_profit(company_profit))  # 262000

# overriding
print('----------- Overriding ------------')
emp_ahmed.print_person_details()

print('-------- Polymorphism -----------')
def print_data_for_all(person):     # # person: reference variable refer to object    parameter name not type
    if isinstance(person, Employee):
        print('This is Employee object')
        print('Person id = ', person.person_id)
        print('Person name = ', person.person_name)
        print('Monthly net salary = ', person.calc_monthly_net_salary())
        print('Monthly net salary = ', person.calc_annual_net_salary())
        person.print_person_details()
    elif isinstance(person, Manager):
        print('This is Manager object')
        print('Person id = ', person.person_id)
        print('Person name = ', person.person_name)
        print('Monthly net salary = ', person.calc_monthly_net_salary())
        print('Monthly net salary = ', person.calc_annual_net_salary())
    else:
        print('Unknown object - invalid')


# test call function
print_data_for_all(emp_ahmed)
print_data_for_all(mgr_khaled)

# Abstraction
# # [ abstract class ] : it is the class that cannot be instantiated
# # [ abstract function ] : it is a function without body must be located in abstract class
# # this function must must be overridden in all children classes
print('----- Abstraction ---------')
emp_ahmed.calc_expenses()
mgr_khaled.calc_expenses()
