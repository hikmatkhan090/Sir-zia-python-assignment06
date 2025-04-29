class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def display(self):
        return f"{self.name} is a {self.position}."

class Department:
    def __init__(self, department_name, employee: Employee):
        self.department_name = department_name
        self.employee = employee  

    def show_department_info(self):
        return f"Department: {self.department_name}\nEmployee Info: {self.employee.display()}"

# Creating an Employee object
emp = Employee("John Doe", "Software Engineer")

# Creating a Department object that references the Employee object
dept = Department("IT", emp)

# Showing information from Department
print(dept.show_department_info())

# Employee can exist independently of Department
print(emp.display())  
