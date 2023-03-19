# final = []

numbers = [int(i) for i in list(map(int, input().split())) if i % 2 == 0]
average = sum(numbers) / len(numbers)
final = [num + 1 if num > average else num - 1 for num in numbers]

print(*final, sep=" ")