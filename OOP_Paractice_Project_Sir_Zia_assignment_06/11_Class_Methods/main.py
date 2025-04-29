class Book:
    # Class variable
    total_books = 0
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        
        cls.total_books += 1
        print(f"Total books: {cls.total_books}")

# Creating Book objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

# Checking total_books after creating books
print(f"Final total books count: {Book.total_books}")
