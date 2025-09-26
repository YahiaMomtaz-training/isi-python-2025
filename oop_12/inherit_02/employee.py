from oop_12.inherit_02.person import Person

class Employee(Person):
    def __init__(self, person_id=None, person_name=None, person_gross_salary=None, person_job=None,
                 over_time_rate=None , over_time_hours=None):
        # call parent constructor
        super().__init__(person_id, person_name, person_gross_salary, person_job)
        self.over_time_rate = over_time_rate
        self.over_time_hours = over_time_hours

    def calc_monthly_net_salary(self):
        return (self.person_gross_salary - self.person_gross_salary * 0.1
                + self.over_time_hours * self.over_time_rate)

    def calc_annual_net_salary(self):
        return self.calc_monthly_net_salary() * 12

# overriding
    def print_person_details(self):
        super().print_person_details()
        print(self.calc_monthly_net_salary())
        print(self.calc_annual_net_salary())

    # overriding
    def calc_expenses(self):
        print('This is calc expenses for employee object')

