class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # Public variable
        self._salary = salary       # Protected variable
        self.__ssn = ssn            # Private variable

# Object creation
emp = Employee("John Doe", 50000, "123-45-6789")

# Accessing Public Variable
print(f"Name: {emp.name}")  
# Accessing Protected Variable
print(f"Salary: {emp._salary}") 

# Accessing Private Variable (This will cause an error!)
try:
    print(f"SSN: {emp.__ssn}")  
except AttributeError as e:
    print(f"Error: {e}")

print(f"SSN (via name mangling): {emp._Employee__ssn}")
