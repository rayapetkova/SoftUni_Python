pairs = int(input())
left_sum = 0
right_sum = 0

for i in range(1, pairs + 1):
    number = int(input())
    left_sum = left_sum + number
for i1 in range(1, pairs + 1):
    number1 = int(input())
    right_sum = right_sum + number1

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")