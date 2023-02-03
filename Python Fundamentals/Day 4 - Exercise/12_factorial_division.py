def result(num1, num2):
    sum1 = 1
    sum2 = 1
    for i in range(2, num1 + 1):
        sum1 *= i
    for j in range(2, num2 + 1):
        sum2 *= j
    total = sum1 / sum2
    return total


current_num1 = int(input())
current_num2 = int(input())
print(f"{(result(current_num1, current_num2)):.2f}")