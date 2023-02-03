def multiplication(a, b, c):
    lst = [a, b, c]
    negatives = 0
    if a == 0 or b == 0 or c == 0:
        return "zero"
    if a > 0 and b > 0 and c > 0:
        return "positive"
    for i in lst:
        if i < 0:
            negatives += 1
    if negatives == 1 or negatives == 3:
        return "negative"
    if negatives == 2:
        return "positive"


current_a = int(input())
current_b = int(input())
current_c = int(input())
print(multiplication(current_a, current_b, current_c))