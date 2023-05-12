n, m = tuple(map(int, input().split()))
first_set, second_set = set(), set()

for i in range(n):
    first_set.add(int(input()))

for j in range(m):
    second_set.add(int(input()))

print(*first_set.intersection(second_set), sep="\n")
