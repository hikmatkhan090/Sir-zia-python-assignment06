class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  
    @property
    def price(self):
        print("💰 Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        print("✏️ Setting price...")
        if value < 0:
            raise ValueError("🚫 Price cannot be negative!")
        self._price = value

    @price.deleter
    def price(self):
        print("🗑️ Deleting price...")
        del self._price


item = Product("Laptop", 1200)


print(f"Price: ${item.price}")


item.price = 1500
print(f"Updated Price: ${item.price}")


try:
    item.price = -500
except ValueError as e:
    print(e)


del item.price

# 🔍 Try accessing after deletion (will raise AttributeError)
try:
    print(item.price)
except AttributeError as e:
    print(f"⚠️ Error: {e}")
