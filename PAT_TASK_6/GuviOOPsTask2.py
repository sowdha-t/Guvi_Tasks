"""Employee Management
Create a Base Class Employee with attributes like name, salary, and a method calculate_salary().
Inherit from this class to create subclasses RegularEmployee, ContractEmployee, and Manager.
Each subclass should have specific attributes and calculation of salary
Implement Inheritance and Polymorphism to calculate the salary of different employee types based
on their specific attributes and rules

"""

# Base Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


# Subclass : Regular Employee
class RegularEmployee(Employee):
    employee_type = "Regular"
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)   # calls Parent Class
        self.bonus = bonus

    def calculate_salary(self):
        # Regular employees get base salary + bonus
        return self.salary + self.bonus


# Subclass : Contract Employee
class ContractEmployee(Employee):
    employee_type = "Contract"
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, salary=0)  # no fixed salary
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        # Contract employees are paid by the hour
        return self.hourly_rate * self.hours_worked


# Subclass : Manager
class Manager(Employee):
    employee_type = "Manager"
    def __init__(self, name, salary, allowance):
        super().__init__(name, salary)
        self.allowance = allowance

    def calculate_salary(self):
        # Managers get base salary + fixed allowance
        return self.salary + self.allowance


# ----  Creating employee objects----
employees = [
    RegularEmployee("Mahi", 30000, 2000),
    ContractEmployee("Devi", 500, 160),
    Manager("Durai", 60000, 10000)
]

for emp in employees:
    # Same method name (calculate_salary), different behavior per class = Polymorphism
    print(f"{emp.name} ({emp.employee_type}) -> Salary: {emp.calculate_salary()}")
