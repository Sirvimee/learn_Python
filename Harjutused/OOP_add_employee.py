"""
Loo kaks klassi Employee def __init__(self, name, position)  ning Company def __init__(self, name, employees=None).
Company klassis realiseerida meetod def add_employee().
"""


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position


class Company:
    def __init__(self, name, employees=None):
        self.name = name
        self.employees = employees if employees is not None else []

    def add_employee(self, employee):
        if self.employees is None:
            self.employees = []
        self.employees.append(employee)


company3 = Company("ABCDEF")
for employee in company3.employees:
    print(f"{employee.name}, {employee.position}")
