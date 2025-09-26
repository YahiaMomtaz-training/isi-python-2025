
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, person_id=None, person_name=None, person_gross_salary=None, person_job=None):
        self.person_id = person_id
        self.person_name = person_name
        self.person_gross_salary = person_gross_salary
        self.person_job = person_job

    def print_person_details(self):
        print('id = ', self.person_id)
        print('name = ', self.person_name)

    # abstract methods
    @abstractmethod
    def calc_expenses(self):
        pass
