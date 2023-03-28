numbers, multiplier = list(map(int, input().split())), int(input())
print(*[n * multiplier for n in numbers], sep=" ")