username = input()
password = input()
entered_password = input()

while entered_password != password:
    entered_password = input()

    if entered_password == password:
        break
print(f"Welcome {username}!")