class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person's name is {self.name}")

# Derived Class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  
        self.subject = subject
        print(f"Teacher teaches {self.subject}")

teacher = Teacher("Mr. Smith", "Mathematics")
