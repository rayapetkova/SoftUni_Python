n = int(input())
result = 0

for i in range(1, n + 1):
    letter = input()
    symbol_in_number = ord(letter)
    result += symbol_in_number

print(f"The sum equals: {result}")