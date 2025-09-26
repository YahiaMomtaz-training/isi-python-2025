from oop_12.inherit_02.person import Person

class Manager(Person):
    def __init__(self, person_id, person_name, person_gross_salary, person_job, profit_percentage):
        super().__init__(person_id, person_name, person_gross_salary, person_job)
        self.profit_percentage = profit_percentage

    # extra methods
    def calc_monthly_net_salary(self):
        tax = 10
        return self.person_gross_salary - self.person_gross_salary * tax / 100

    def calc_annual_net_salary(self):
        return self.calc_monthly_net_salary() * 12

    def calc_annual_net_salary_profit(self, company_profit):
        return self.calc_annual_net_salary() + company_profit * self.profit_percentage / 100

# overriding method
    def calc_expenses(self):
        print('This is calc expenses for Manager object')

