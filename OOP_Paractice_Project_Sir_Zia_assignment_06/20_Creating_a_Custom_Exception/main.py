class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"🚫 Invalid Age: {age}. Age must be 18 or above.")
        self.age = age

# Step 2: Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    print(f"✅ Access granted. Welcome! Age: {age} 🎉")

#  Step 3: Main Program
def main():
    try:
        age_input = int(input("🔍 Enter your age: "))
        check_age(age_input)
    except InvalidAgeError as e:
        print(f"❌ Error: {e}")
    except ValueError:
        print("⚠️ Please enter a valid number.")
    finally:
        print("🛑 Process complete.")


if __name__ == "__main__":
    main()
