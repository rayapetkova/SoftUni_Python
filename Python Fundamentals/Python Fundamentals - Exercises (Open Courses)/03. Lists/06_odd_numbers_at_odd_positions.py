numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    if i % 2 != 0 and numbers[i] % 2 != 0:
        print(f"Index {i} -> {numbers[i]}")