class Employee:
    countEmployees = 0
    salaries = []

    # Default constructor function
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

        # appending salaries to the list
        Employee.salaries.append(self.salary)
        Employee.countEmployees = self.countEmployees + 1

    # Function to average salary
    def avgsalary(self, salaries):
        length = len(salaries)
        totalsalary = 0
        for salary in salaries:
            totalsalary = totalsalary + salary
        print("Average Salaries of all Employees = ", totalsalary / length)


# Fulltime Employee class
class FulltimeEmployee(Employee):

    def __init__(self, empId, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)
        self.empId = empId


Emp1 = Employee("Tejaswi", "Guturu", 5000, "CSE")
Emp2 = Employee("Pooja", "Gopu", 8000, "ECE")
FulEmp1 = FulltimeEmployee(157, "Pujitha", "Sakh", 10000, "Civil")

print("Employee1 Name is: ", Emp1.name)
print("Employee2 Name is: ", Emp2.name)
print("Fulltime Employee1 Name is: ", FulEmp1.name)

# Access data member using Fulltime Employee class
print("Number of Employees: ", Employee.countEmployees)
FulEmp1.avgsalary(FulltimeEmployee.salaries)
