class Counter:
    # Class variable to keep track of the number of objects
    count = 0

    def __init__(self):
        # Each time an object is created, increment the count
        Counter.count += 1

    @classmethod
    def display_count(cls):
        # Method to display the number of objects created
        print(f"Total objects created: {cls.count} 🎉")

# Create objects of Counter class
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Display the count using class method
Counter.display_count()  # Output: Total objects created: 3 🎉
