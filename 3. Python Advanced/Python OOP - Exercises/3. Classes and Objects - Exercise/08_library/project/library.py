from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}  # {'author': ['book_1', 'book_2'...]}
        self.rented_books = {}  # {'Pesho': {'book_1': 4, 'book_2': 10}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        for c_author, c_books in self.books_available.items():
            if book_name in c_books:
                user.books.append(book_name)
                self.books_available[author].remove(book_name)

                if user.username not in self.rented_books.keys():
                    self.rented_books[user.username] = {book_name: days_to_return}
                else:
                    self.rented_books[user.username][book_name] = days_to_return

                return f"{book_name} successfully rented for the next {days_to_return} days!"

        days = 0
        for key, value in self.rented_books.items():
            for c_book, c_days in value.items():
                if c_book == book_name:
                    days = c_days

        return f'The book "{book_name}" is already rented and will be available in {days} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)

            del self.rented_books[user.username][book_name]

        else:
            return f"{user.username} doesn't have this book in his/her records!"

