class MathUtils:
    @staticmethod
    def add(a: float, b: float) -> float:
        """➕ Do numbers ka total nikalta hai"""
        print(f"🧮 Adding: {a} + {b}")
        return a + b


result1 = MathUtils.add(15, 27)
print(f"🔢 Result 1: {result1}")

result2 = MathUtils.add(100.5, 200.75)
print(f"🔢 Result 2: {result2}")
