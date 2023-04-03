num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):
    even_sum = 0
    odd_sum = 0
    current_num = str(i)
    for j in range(0, len(current_num)):
        digit = int(current_num[j])
        if j % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    if even_sum == odd_sum:
        print(current_num, end=" ")
