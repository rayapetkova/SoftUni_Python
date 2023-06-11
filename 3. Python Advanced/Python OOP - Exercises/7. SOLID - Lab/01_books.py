class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title: str):
        for book in self.books:
            if book.title == title:
                return book

        return f"There is no such book in the library"

    def __repr__(self):
        return f"This is {self.name} Library. It is located in {self.location}. " \
               f"\nBooks in the library: \n{', '.join(str(b) for b in self.books)}"


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return f"This is {self.title} book by {self.author}"


# Test code:

# book1 = Book("Test book1", "Test Author1")
# book2 = Book("Test book2", "Test Author2")
# library = Library("Test Library Name", "Test location")
# library.add_book(book1)
# library.add_book(book2)
# print(library)
# print(library.find_book("Test book1"))
# print(library.find_book("Invalid title"))
