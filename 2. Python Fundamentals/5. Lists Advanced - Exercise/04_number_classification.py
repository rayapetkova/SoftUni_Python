#1

numbers = [int(i) for i in input().split(", ")]

positives = [str(j) for j in numbers if j >= 0]
negatives = [str(j) for j in numbers if j < 0]
evens = [str(j) for j in numbers if j % 2 == 0]
odds = [str(j) for j in numbers if j % 2 != 0]

print(f"Positive: {', '.join(positives)}")
print(f"Negative: {', '.join(negatives)}")
print(f"Even: {', '.join(evens)}")
print(f"Odd: {', '.join(odds)}")





#2
#
# numbers = [int(i) for i in input().split(", ")]
#
#
# def positives():
#     p_numbers = [str(j) for j in numbers if j >= 0]
#     return f"Positive: {', '.join(p_numbers)}"
#
#
# def negatives():
#     n_numbers = [str(j) for j in numbers if j < 0]
#     return f"Negative: {', '.join(n_numbers)}"
#
#
# def evens():
#     e_numbers = [str(j) for j in numbers if j % 2 == 0]
#     return f"Even: {', '.join(e_numbers)}"
#
#
# def odds():
#     o_numbers = [str(j) for j in numbers if j % 2 != 0]
#     return f"Odd: {', '.join(o_numbers)}"
#
#
# print(positives())
# print(negatives())
# print(evens())
# print(odds())
