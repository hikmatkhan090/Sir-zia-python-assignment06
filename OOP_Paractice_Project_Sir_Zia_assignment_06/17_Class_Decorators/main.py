def add_greeting(cls):

    
    # Adding the greet method to the class
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  
    return cls

# Applying the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hi, my name is {self.name}"

# Creating an instance of Person
person = Person("Ali")

# Calling the greet method added by the decorator
print(person.greet())  
# Calling other methods of the class
print(person.introduce())  
