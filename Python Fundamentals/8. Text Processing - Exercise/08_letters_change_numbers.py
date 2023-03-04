text = input().split()


def first_letter(first, num):
    if first.isupper():
        num /= ord(first) - 64
    elif first.islower():
        num *= ord(first) - 96
    return num


def last_letter(last, num):
    if last.isupper():
        num -= ord(last) - 64
    elif last.islower():
        num += ord(last) - 96
    return num


total = 0
for word in text:
    number = int(word[1:-1])
    number = first_letter(word[0], number)
    number = last_letter(word[-1], number)
    total += number

print(f"{total:.2f}")




#2
#
# text = input().split()
#
# total = 0
# for word in text:
#     number = int(word[1:-1])
#     if word[0].isupper():
#         number /= ord(word[0]) - 64
#     elif word[0].islower():
#         number *= ord(word[0]) - 96
#
#     if word[-1].isupper():
#         number -= ord(word[-1]) - 64
#     elif word[-1].islower():
#         number += ord(word[-1]) - 96
#     total += number
#
# print(f"{total:.2f}")
