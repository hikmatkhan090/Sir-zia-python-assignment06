class Dog:
    def __init__(self, name, breed):
        
        self.name = name
        self.breed = breed

    def bark(self):

        print(f"{self.name} the {self.breed} says Woof!")

# Creating objects (instances) of the Dog class
dog1 = Dog("Max", "Golden Retriever")
dog2 = Dog("Bella", "Bulldog")

# Calling the instance method 'bark' for both dogs
dog1.bark() 
dog2.bark()  