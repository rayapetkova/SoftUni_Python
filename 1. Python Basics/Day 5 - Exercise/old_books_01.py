favourite_book = input()

counter_books = 0

while True:
    book = input()
    counter_books = counter_books + 1
    if book == favourite_book:
        counter_books = counter_books - 1
        print(f"You checked {counter_books} books and found it.")
        break
    if book == "No More Books":
        counter_books = counter_books - 1
        print(f"The book you search is not here!")
        print(f"You checked {counter_books} books.")
        break