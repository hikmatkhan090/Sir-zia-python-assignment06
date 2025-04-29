class Engine:
    def __init__(self, type_of_engine):
        self.type_of_engine = type_of_engine
    
    def start(self):
        return f"Starting the {self.type_of_engine} engine."

class Car:
    def __init__(self, brand, engine: Engine):
        self.brand = brand
        self.engine = engine  

    def drive(self):
        return f"The {self.brand} car is driving with {self.engine.start()}"

# Creating an Engine object
engine = Engine("V8")

# Passing Engine object to Car object
car = Car("Toyota", engine)

# Accessing Engine's method via Car
print(car.drive())  
