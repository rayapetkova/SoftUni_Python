numbers = list(map(int, input().split()))
print(len([num for num in numbers if num % 2 != 0]))