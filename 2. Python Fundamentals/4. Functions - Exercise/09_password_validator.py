def validator(password):
    counter = 0
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        print("Password must consist only of letters and digits")
    for i in password:
        if i.isdigit():
            counter += 1
    if counter < 2:
        print("Password must have at least 2 digits")
    if 6 <= len(password) <= 10 and password.isalnum() and counter >= 2:
        print("Password is valid")


current_password = input()
validator(current_password)
