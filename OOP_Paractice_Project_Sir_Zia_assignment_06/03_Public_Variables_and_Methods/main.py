class Car:
    def __init__(self, brand: str, model: str, year: int):
        # Public variables
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0  

    # Public method to start the car
    def start(self):
        print(f"🔑 {self.brand} {self.model} ({self.year}) is starting... 🚗💨")

    # Public method to drive the car
    def drive(self, km: int):
        self.mileage += km
        print(f"🛣️ Drove {km} km. Total mileage: {self.mileage} km")

    # Public method to display full car info
    def display_info(self):
        print("📋 Car Information:")
        print(f"🚘 Brand: {self.brand}")
        print(f"📌 Model: {self.model}")
        print(f"📅 Year: {self.year}")
        print(f"📊 Mileage: {self.mileage} km")

# Creating multiple cars
car1 = Car("Tesla", "Model S", 2022)
car2 = Car("Ford", "Mustang", 2020)

# Using public methods
car1.start()
car1.drive(120)
car1.display_info()

print("\n-----------------------\n")

car2.start()
car2.drive(75)
car2.display_info()
