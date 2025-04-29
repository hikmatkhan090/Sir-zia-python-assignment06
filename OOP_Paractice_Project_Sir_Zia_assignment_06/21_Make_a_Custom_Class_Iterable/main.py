class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        print(f"🚀 Starting countdown from {self.start}...")
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return f"⏳ {value}..."

# Use the Countdown class in a for-loop
def main():
    countdown = Countdown(5) 
    for number in countdown:
        print(number)
    print("🎉 Countdown complete!")

if __name__ == "__main__":
    main()
