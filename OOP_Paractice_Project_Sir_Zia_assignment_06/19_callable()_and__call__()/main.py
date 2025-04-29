class Multiplier:
    def __init__(self, factor):
        self.factor = factor
        print(f"🎯 Multiplier initialized with factor: {self.factor}")

    def __call__(self, number):
        result = self.factor * number
        print(f"🔢 Calling object like a function: {self.factor} × {number} = {result}")
        return result

# ✅ Create instance
times_five = Multiplier(5)

# ✅ Test with callable()
print("🧪 Is 'times_five' callable?", callable(times_five))  # Output: True

# ✅ Use like a function
output = times_five(10)  
print(f"✅ Final Output: {output}")
