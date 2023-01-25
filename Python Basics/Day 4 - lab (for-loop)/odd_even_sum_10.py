n = int(input())
even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        number = int(input())
        even_sum = even_sum + number
    else:
        number1 = int(input())
        odd_sum = odd_sum + number1

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {abs(even_sum - odd_sum)}")