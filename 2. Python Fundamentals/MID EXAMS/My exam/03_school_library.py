books = input().split("&")

while True:
    line = input()
    if line == "Done":
        break
    command = line.split(" | ")
    if command[0] == "Add Book":
        book = command[1]
        if book not in books:
            books.insert(0, book)
    elif command[0] == "Take Book":
        book = command[1]
        if book in books:
            books.remove(book)
    elif command[0] == "Swap Books":
        first_book = command[1]
        second_book = command[2]
        if first_book in books and second_book in books:
            first_book_idx = books.index(first_book)
            second_book_idx = books.index(second_book)
            books[first_book_idx], books[second_book_idx] = books[second_book_idx], books[first_book_idx]
    elif command[0] == "Insert Book":
        book = command[1]
        if book not in books:
            books.append(book)
    elif command[0] == "Check Book":
        idx = int(command[1])
        if 0 <= idx < len(books):
            print(books[idx])

print(", ".join(books))