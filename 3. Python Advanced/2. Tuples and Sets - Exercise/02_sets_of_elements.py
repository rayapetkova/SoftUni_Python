n, m = tuple(map(int, input().split()))
first_set = set()
second_set = set()

for i in range(n):
    first_set.add(int(input()))

for j in range(m):
    second_set.add(int(input()))

same_values = first_set.intersection(second_set)
[print(num) for num in same_values]