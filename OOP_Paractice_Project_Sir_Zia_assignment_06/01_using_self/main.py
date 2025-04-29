class Student:
    def __init__(self, name, marks):
        self.name = name  
        self.marks = marks  
    
    def display(self):
        
        # Display student details with emojis
        print(f"🎓 Student Name: {self.name}")
        print(f"📚 Marks: {self.marks}")
        if self.marks >= 90:
            print("🏅 Grade: A+")
        elif self.marks >= 75:
            print("🌟 Grade: A")
        elif self.marks >= 60:
            print("✅ Grade: B")
        else:
            print("⚠️ Grade: C")

# Example usage
student1 = Student("Hikmat Khan", 85)
student1.display()

student2 = Student("Ali Ahmed", 95)
student2.display()
