class Employee:
    number_of_employees = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.number_of_employees += 1

    def average_salary(self, *salaries):
        return sum(salaries) / len(salaries)


class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department, hours_worked):
        super().__init__(name, family, salary, department)
        self.hours_worked = hours_worked


# Create instances
e1 = Employee("shiva raju", "Family1", 70000, "Devops Engineer")
e2 = Employee("rahul", "Family2", 60000, "Data Engineer")
e3 = Employee("rishith","Family3",80000,"Salesforce Developer")

full_time_employee = FullTimeEmployee("ram", "Family3", 70000, "Java Developer", 60)

# Call member functions

print(f"Number of Employees: {Employee.number_of_employees}")
average_salary_employee = e1.average_salary(e2.salary)
print(f"Average Salary of Employees: {average_salary_employee}")

average_salary_full_time_employee = full_time_employee.average_salary(e1.salary, e2.salary)
print(f"Average Salary of Employees including FullTimeEmployee: {average_salary_full_time_employee}")