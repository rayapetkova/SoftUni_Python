n = int(input())
first_list = []
second_list = []

for i in range(n):
    num = int(input())
    if num >= 0:
        first_list.append(num)
    else:
        second_list.append(num)

print(first_list)
print(second_list)
print(f"Count of positives: {len(first_list)}\nSum of negatives: {sum(int(j) for j in second_list)}")