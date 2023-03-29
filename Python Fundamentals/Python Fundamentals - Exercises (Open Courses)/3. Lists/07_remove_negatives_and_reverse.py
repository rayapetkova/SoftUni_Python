numbers = list(map(int, input().split()))
numbers = [num for num in numbers if num >= 0]

if numbers:
    print(*numbers[::-1], sep=" ")
else:
    print(f"empty")