class Logger:
    def __init__(self):
        print("🟢 Logger Initialized: Object created successfully!")

    def __del__(self):
        print("🔴 Logger Terminated: Object destroyed properly!")


print("📁 Creating logger instance...")
logger = Logger()

print("📁 Doing some tasks... ⏳")


print("📁 Deleting logger instance... 🗑️")
del logger  

print("✅ Program Completed.")
