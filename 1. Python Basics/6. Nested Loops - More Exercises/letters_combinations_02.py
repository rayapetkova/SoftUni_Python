start = input()
end = input()
some_letter = input()

counter = 0

for first_letter in range(ord(start), ord(end) + 1):
    for second_letter in range(ord(start), ord(end) + 1):
        for third_letter in range(ord(start), ord(end) + 1):
            if chr(first_letter) != some_letter and chr(second_letter) != some_letter and chr(third_letter) != some_letter:
                counter = counter + 1
                print(f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}", end=" ")

print(counter)