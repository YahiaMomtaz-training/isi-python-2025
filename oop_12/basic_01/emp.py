class Emp:
    # Constructor
    def __init__(self, employee_id = None, employee_name = None, employee_salary = None, employee_job = None):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_salary = employee_salary
        self.employee_job = employee_job
        self.employee_city = 'cairo'

    # functions
    def calc_monthly_net_salary(self):
        tax = 10
        return self.employee_salary - self.employee_salary * tax / 100

    def calc_annual_net_salary(self):
        return self.calc_monthly_net_salary() * 12